#
# Compartment class
#

class Compartment:

    def __init__(self, c_type, rate, volume) -> None:
        self.c_type = c_type  # Dosing or peripheral
        self.rate = rate
        self.volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if self.c_type == "dosing":
            self._volume = 0
        elif self.c_type == "peripheral":
            self._volume = volume
        else:
            raise ValueError("'c_type' must be 'dosing' or 'peripheral'")