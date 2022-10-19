#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """

    # def __init__(self, dosing_mode, rate, dosing_strategy):
    def __init__(self, dosing_strategy):
        """A PK model

        Args:
            dosing_mode (_type_): "constant" or "spiked"
            rate (_type_): rate of drug administration, ignore if "spiked"
            dosing_strategy (_type_): list of tuples specifying intervals
                between time and the dose administered -- TO SPECIFY LATER.
                Ignore if dosing mode is "constant"
        """
        # self.dosing_mode = dosing_mode
        # self.rate = rate
        self.dosing_strategy = dosing_strategy

    @property
    def dosing_mode(self):
        return self._dosing_mode

    @dosing_mode.setter
    def dosing_mode(self, dosing_mode):
        # Validate that the dosing mode provided is valid before setting; if not
        # raise error
        self._dosing_mode = dosing_mode

    # Implement similar validation using setters and getters for rate and
    # dosing strategy

