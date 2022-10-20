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
        if not isinstance(dosing_strategy, list):
            raise TypeError("Dosing strategy must be list of Dose objects.")
        elif len(dosing_strategy) == 0:
            raise ValueError("A dosing strategy must be specified")
        else:
            for dose in dosing_strategy:
                if not isinstance(dose, Dose):
                    raise TypeError("List must contain Dose or Spiked objects.")

