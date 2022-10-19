#
# Model class
#

class Model:
    
    def __init__(
        self,
        name="PK model",
        dosing=None,
        volume=1,
        clearance_rate=1,
        peripherals=None,
        therapeutic_max=None,
        therapeutic_min=None,
        protocol=None,
    ):
        """A Pharmacokinetic (PK) model

        Args:
            dosing (Compartment): _description_
            volume (float): _description_
            clearance_rate (float): _description_
            peripherals (Compartment): _description_
            therapeutic_max (float): _description_
            therapeutic_min (float): _description_
        """
        self.name = name
        self.dosing = dosing
        self.volume = volume
        self.clearance_rate = clearance_rate
        self.peripherals = peripherals
        self.therapeutic_max = therapeutic_max
        self.therapeutic_min = therapeutic_min
        self.protocol = protocol # TODO: passed to solver?


class Compartment:

    def __init__(self, c_type, rate, volume) -> None:
        self.c_type = c_type # Dosing or compartment
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
