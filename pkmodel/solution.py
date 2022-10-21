#
# Solution class
#
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate


class Solution:
    # def __init__(self, models, protocols, therapeutic_min, therapeutic_max):
    def __init__(self, models, therapeutic_min, therapeutic_max):
        """Defining the system of differential equations and then 
            solving them and plotting them.

         Args:
             models TODO I am not sure what to write here
             therapeutic_min (float): the minimally required drug in a compartment
                for the drug to be effective.
             therapeutic_max (float): the maximally permited mass of drug in a
                compartment before it becomes toxic.        
        """
        self.models = models
        self.therapeutic_min = therapeutic_min
        self.therapeutic_max = therapeutic_max
        # self.protocols = protocols
        self.solutions = {}

    def _dose(self, t, protocol):
        """Applying the dose & protocol that are specified in their respective classes.

         Args:
             t (float): timepoint at which the model is currently at.
             protocol (class): TODO add/check this   
        """
        dosage = 0
        for dose in protocol.dosing_strategy:
            if t > dose.start and t < dose.end:
                dosage += dose.rate
        return dosage

    def _rhs(self, t, y, model):
        """Defining the differential equations of the model.

         Args:
             t (float): timepoint at which the model is currently at.
             y () TODO add/check this
             model (class): TODO add/check this   
        """
        q_c, *q_ps = y
        transitions = []
        for i in range(len(model.peripherals)):
            p = model.peripherals[i]
            q_p = q_ps[i]
            transition = p.rate * (q_c / model.volume - q_p / p.volume)
            transitions.append(transition)

        dqc_dt = self._dose(t, model.protocol) - q_c / model.volume * model.clearance_rate - sum(transitions)
        return [dqc_dt] + transitions

    def solve(self):
        """Finding the mass in each compartment by solving the differential equations.
        """
        # pass
        t_eval = np.linspace(0, 1, 1000)

        for model in self.models:
            y0 = np.array([0.0] + [0.0 for _ in model.peripherals])
            sol = scipy.integrate.solve_ivp(
                fun=lambda t, y: self._rhs(t, y, model),
                t_span=[t_eval[0], t_eval[-1]],
                y0=y0, t_eval=t_eval
            )
            self.solutions[model.name] = sol

    def _make_plot(self):
        """Constructing a single graph showing the mass of drug  the dose & protocol that are specified in their respective classes.    
        """
        fig = plt.figure() # noqa
        for model in self.models:
            sol = self.solutions[model.name]
            plt.plot(sol.t, sol.y[0, :], label=model.name + '- q_c')
            # plt.plot(sol.t, sol.y[1, :], label=model.name + '- q_p1')
            for i in range(1, sol.y.shape[0]):
                plt.plot(sol.t, sol.y[i, :], label=model.name + '- q_p{}'.format(i))
            # if np.max(sol.y) > self.therapeutic_max:
            #     print('Drug concentration of ' + model['name'] + ' exceeds toxic threshold, use lighter dosing')
        [plt.axhline(y=i, linestyle='--') for i in [self.therapeutic_min, self.therapeutic_max]]
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        return plt

    # Implement method that plots the solutions via matplotlib
    def plot(self):
        """Plotting the graph constructed in make_plot.    
        """
        plt = self._make_plot()
        plt.show()

    # Implement method that saves the plots to a specified file path
    def save_plot(self, filepath='pkmodel_plot.png'):
        """Saving the plot constructed in make_plot.    
        """
        plt = self._make_plot()
        plt.savefig(filepath)
