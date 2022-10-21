#
# Dose class
#

from math import inf

class Dose:
    """A dose with a continuous, constant administration rate.

    :param rate: rate at which dose is administered
    :type rate: float
    :param start: time at which dosing begins, defaults to 0
    :type start: float, optional
    :param end: time at which dosing ends, defaults to inf
    :type end: float, optional
    """
    def __init__(self, rate: float, start: float=0, end: float=inf):
        self.start = start
        self.end = end
        self.rate = rate


class SpikeDose(Dose):
    """A discrete dose administered instantaneously at one timepoint.

    :param volume: quantity administered in the dose
    :type volume: float
    :param start: time at which the dose is administered
    :type start: float
    """
    def __init__(self, volume: float, start: float):
        delta = 0.01
        end = start + delta
        rate = volume / delta
        super().__init__(rate, start, end)
