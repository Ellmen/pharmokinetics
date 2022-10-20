#
# Compartment class
#

class Compartment:
    def __init__(self, c_type, rate, volume) -> None:
        """TODO
        
        Args:
            c_type (TODO): Compartment type: Dosing or peripheral compartment.
            rate (float): Flow rate of drug between two compartments.
            volume (float): Volume (mL) inside a compartment.
    """
        self.c_type = c_type  # Dosing or peripheral
        self.rate = rate
        self.volume = volume

    @property
    def volume(self):
        """TODO
    """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """TODO
        
        Args:
            volume (float): Volume (mL) inside a compartment.
        """
        if self.c_type == "dosing":
            self._volume = 0
        elif self.c_type == "peripheral":
            self._volume = volume
        else:
            raise ValueError("'c_type' must be 'dosing' or 'peripheral'")
