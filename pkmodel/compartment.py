#
# Compartment class
#

class Compartment:

    def __init__(self, rate: float, volume: float):
        """A peripheral compartment in a PK model.

        :param rate: the rate constant describing the flux rate between the central and peripheral compartment
        :type rate: float
        :param volume: the volume of the compartment
        :type volume: float
        """
        self.rate = rate
        self.volume = volume
        