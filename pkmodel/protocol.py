#
# Protocol class
#

from pkmodel.dose import Dose, SpikeDose

class Protocol:
    def __init__(self, dosing_strategy):
        """A Pharmacokinetic protocol of doses

        Args:
            dosing_strategy (list): list of doses specifying intervals
                between time and the dose administered.
        """
        self.dosing_strategy = dosing_strategy

    @property
    def dosing_strategy(self):
        return self._dosing_strategy

    @dosing_strategy.setter
    def dosing_strategy(self, dosing_strategy):
        if len(dosing_strategy) == 0:
            raise KeyError("A dosing strategy must be specified")
        if not isinstance(dosing_strategy, list):
            raise TypeError("Dosing strategy must be list of Dose objects.")
        if len(dosing_strategy) == 1:
            if not isinstance(dose, Dose):
                raise KeyError("List must contain Dose or Spiked objects.")
        else: # Greater than 1; must be a spiked dose protocol
            for dose in dosing_strategy:
                if not isinstance(dose, SpikeDose):
                    raise KeyError("All list items must be SpikedDose objects.")
        self._dosing_strategy = dosing_strategy
