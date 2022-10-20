#
# Compartment class
#

class Compartment:

    def __init__(self, c_type, rate, volume) -> None:
        self.c_type = c_type  # Dosing or compartment
        self.rate = rate
        self.volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if self.c_type == "dosing":
            self._volume = 0
        else:
            self._volume = volume