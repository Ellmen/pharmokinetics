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
        """Defining the components of the (PK) model

        Args:
            name (string): name of the model.
            dosing (Compartment): _description_
            volume (float): the volume within a compartment
            clearance_rate (float): rate at which drug is cleared from the central compartment
                into the exterior [mL/h].
            peripherals (Compartment): _description_
            therapeutic_min (float): the minimally required drug in a compartment
                for the drug to be effective.
            therapeutic_max (float): the maximally permited mass of drug in a
                compartment before it becomes toxic. 
        """
        self.name = name
        self.dosing = dosing
        self.volume = volume
        self.clearance_rate = clearance_rate
        self.peripherals = peripherals
        self.therapeutic_max = therapeutic_max
        self.therapeutic_min = therapeutic_min
        self.protocol = protocol  # TODO: passed to solver?
