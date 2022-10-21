#
# Solution class
#
from typing import List
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

from pkmodel.model import Model


class Solution:
    """A collection of PK models and methods required to model and plot
    their behaviour.

    :param models: a list of PK models to compare and solve
    :type models: _type_
    :param therapeutic_max: the upper limit of the therapeutic window, 
        defaults to None
    :type therapeutic_max: float, optional
    :param therapeutic_min: the lower limit of the therapeutic window, 
        defaults to None
    :type therapeutic_min: float, optional
    :param time: timeframe (h) over which the models should be solved for, 
        defaults to 1
    :type time: float, optional
    """
    def __init__(
        self,
        models: List[Model],
        therapeutic_min: float = None,
        therapeutic_max: float = None,
        time: float = 1
    ):
        self.models = models
        self.therapeutic_min = therapeutic_min
        self.therapeutic_max = therapeutic_max
        self.solutions = {}
        self.time = round(time, 2)

    def _dose(self, t, protocol):
        dosage = 0
        for dose in protocol.dosing_strategy:
            if t > dose.start and t < dose.end:
                dosage += dose.rate
        return dosage

    def _rhs(self, t, y, model):
        q_0, q_c, *q_ps = y
        transitions = []
        for i in range(len(model.peripherals)):
            p = model.peripherals[i]
            q_p = q_ps[i]
            transition = p.rate * (q_c / model.volume - q_p / p.volume)
            transitions.append(transition)
        if model.dosing_rate is not None:
            dqc_dt = model.dosing_rate * q_0 - q_c / model.volume * model.clearance_rate - sum(transitions)
            dq0_dt = self._dose(t, model.protocol) - model.dosing_rate * q_0
        else:
            dqc_dt = self._dose(t, model.protocol) - q_c / model.volume * model.clearance_rate - sum(transitions)
            dq0_dt = 0

        return [dq0_dt, dqc_dt] + transitions

    def solve(self):
        """Solve the differential equations required to model the systems.
        """
        t_eval = np.linspace(0, self.time, int(self.time * 10000))

        for model in self.models:
            y0 = np.array([0.0, 0.0] + [0.0 for _ in model.peripherals])
            sol = scipy.integrate.solve_ivp(
                fun=lambda t, y: self._rhs(t, y, model),
                t_span=[t_eval[0], t_eval[-1]],
                y0=y0,
                t_eval=t_eval,
                max_step=0.001,
            )
            self.solutions[model.name] = sol

    def _make_plot(self):
        if self.solutions == {}:
            raise ValueError("Must run s.solve() before plotting solutions")
        fig = plt.figure(figsize=(8, 6)) # noqa
        for model in self.models:
            sol = self.solutions[model.name]
            if model.dosing_rate is not None:
                plt.plot(sol.t, sol.y[0, :], label=model.name + ' - $q_0$')
            plt.plot(sol.t, sol.y[1, :], label=model.name + ' - $q_c$')
            for i in range(2, sol.y.shape[0]):
                plt.plot(sol.t, sol.y[i, :], label=model.name + ' - $q_{{p{}}}$'.format(i - 1))
        [plt.axhline(y=i, linestyle='--', alpha=0.2) for i in [self.therapeutic_min, self.therapeutic_max] if i is not None]
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.xlim(0, self.time)
        plt.ylim(bottom=0)
        if self.therapeutic_max is not None and self.therapeutic_min is not None:
            plt.fill_between([0, self.time], self.therapeutic_max, self.therapeutic_min, color="lime", alpha= 0.1)
        plt.legend(loc="upper right")
        return plt

    def plot(self):
        """Visualise the behaviour of the system on a graph
        """
        plt = self._make_plot()
        plt.show()

    def save_plot(self, filepath='pkmodel_plot.png'):
        """Save the plot in a chosen directory

        :param filepath: filepath of where the plot should be saved, defaults 
            to 'pkmodel_plot.png'
        :type filepath: str, optional
        """
        plt = self._make_plot()
        plt.savefig(filepath)
