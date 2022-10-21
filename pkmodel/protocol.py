#
# Protocol class
#

from typing import List
from pkmodel.dose import Dose, SpikeDose

class Protocol:
    """A Pharmacokinetic protocol describing the doses to be administered.

    Args:
        dosing_strategy (list[Dose]): list of Dose objects describing the
            dosing strategy
    """
    def __init__(self, dosing_strategy: List[Dose]):
        self.dosing_strategy = dosing_strategy
        if not isinstance(dosing_strategy, list):
            raise TypeError("Dosing strategy must be list of Dose objects.")
        elif len(dosing_strategy) == 0:
            raise ValueError("A dosing strategy must be specified")
        else:
            for dose in dosing_strategy:
                if not isinstance(dose, Dose):
                    raise TypeError("List must contain Dose or Spiked objects.")