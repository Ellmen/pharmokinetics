#
# Model class
#

from typing import List
from pkmodel.compartment import Compartment
from pkmodel.protocol import Protocol

class Model:

    """A pharamcokinetic model describing a central compartment and 
    optional peripheral and dosing compartments, as well as a dosing
    protocol.

    :param name: the name of the PK model
    :type name: str
    :param volume: the volume of the central compartment, defaults to 1
    :type volume: float
    :param clearance_rate: the rate constant describing the efflux of drug
        from the central compartment, out of the system, defaults to 1
    :type clearance_rate: float
    :param protocol: a protocol object describing the dosing regime, 
        defaults to None
    :type protocol: Protocol
    :param dosing_rate: the rate constant describing the flow of drug from 
        a dosing compartment into the central compartment. If none is
        provided, the model describes instantaneous administration to the 
        central compartment i.e. IV injection, defaults to None
    :type dosing_rate: float, optional
    :param peripherals: a list of peripheral compartments in the system, 
        defaults to None
    :type peripherals: List[Compartment], optional
    """
    def __init__(
        self,
        name: str,
        volume: float,
        clearance_rate: float,
        protocol: Protocol,
        dosing_rate: float = None,
        peripherals: List[Compartment] = None,
    ):
        self.name = name
        self.dosing_rate = dosing_rate
        self.volume = volume
        self.clearance_rate = clearance_rate
        self.peripherals = [] if peripherals is None else peripherals
        self.protocol = protocol
