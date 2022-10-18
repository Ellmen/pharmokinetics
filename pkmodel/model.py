#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
   
    for i <= number_peripherals #with number_peripherals an integer float chosen by the user
    
        if chosen_model== intravenous_bolus

        dq_c/dt=Dose(t) -q_c/V_c*CL-Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
        d_{qp1}/dt=Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
        #TODO: add code to include possibility for more than 1 peripheral compartment

        elif chosen_model==subcutaneous

        d_{q0}/dt=Dose(t)-k_a*q_0
        dq_c/dt=k_aq*q_0-q_c/V_c*CL-Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
        #TODO: add code to include possibility for more than 1 peripheral compartment
        d_{qp1}/dt=Q_{p1}*(q_c/V_c - q_{p1}/V_{p1})
        
    
    def __init__(self, value=42):
        self.value = value

