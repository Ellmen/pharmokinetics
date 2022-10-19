#
# Model class
#

class Model:
    # for i <= number_peripherals #with number_peripherals an integer float chosen by the user
    
    #     if chosen_model== intravenous_bolus

    #     dq_c/dt=Dose(t) -q_c/V_c*CL-Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
    #     d_{qp1}/dt=Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
    #     #TODO: add code to include possibility for more than 1 peripheral compartment

    #     elif chosen_model==subcutaneous

    #     d_{q0}/dt=Dose(t)-k_a*q_0
    #     dq_c/dt=k_aq*q_0-q_c/V_c*CL-Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
    #     #TODO: add code to include possibility for more than 1 peripheral compartment
    #     d_{qp1}/dt=Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
        
    
    def __init__(self, dosing=None, peripherals=None, therapeutic_max=None, therapeutic_min=None):
        """A Pharmacokinetic (PK) model

        Args:
            dosing (Compartment): _description_
            peripherals (Compartment): _description_
            therapeutic_max (float): _description_
            therapeutic_min (float): _description_
        """
        self.dosing = dosing
        self.peripherals = peripherals
        self.therapeutic_max = therapeutic_max
        self.therapeutic_min = therapeutic_min
        
class Compartment:

    def __init__(self, type, rate, volume, quantity) -> None:
        self.type = type
        self.rate = rate
        self.volume = volume
        self.quantity = quantity
    
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, volume):
        if self.type == "dosing":
            self._volume = 0
        else:
            self._volume = volume
