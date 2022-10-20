from math import inf


class Dose:
    def __init__(self, rate, start=0, end=inf):
        """Describe continuously administered dose

        Args:
            rate (list): list of doses specifying intervals
                between time and the dose administered.
            start (float): timepoint at which drug administration
                starts, default at the start of the model.
            end (float): timepoint at which drug administration
                ends, default is administration that never ends.
        """
        self.start = start
        self.end = end
        self.rate = rate


class SpikeDose(Dose):
    def __init__(self, volume, start):
        """Describe instantenously administered drug dose(s)

        Args:
            volume (float): the total administered drug for a single
                instantenous injection.
            start (float): timepoint at which drug administration
                starts.
        """
        delta = 0.01
        end = start + delta
        rate = volume / delta
        super().__init__(rate, start, end)


