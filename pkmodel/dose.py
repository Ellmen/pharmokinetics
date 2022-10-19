from math import inf


class Dose:
    def __init__(self, rate, start=0, end=inf):
        self.start = start
        self.end = end
        self.rate = rate


class SpikeDose(Dose):
    def __init__(self, volume, start):
        delta = 0.01
        end = start + delta
        rate = volume / delta
        super().__init__(rate, start, end)


