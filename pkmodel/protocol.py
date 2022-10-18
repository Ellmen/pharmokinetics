#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    
       Dose(t)=Dose_initial+[Dose_pulsed if t/T_{interval}== int] + Dose_continuous*t#with all these Dose_ being set by the user and the if statement to make dosed injection possible

    def __init__(self, value=43):
        self.value = value

