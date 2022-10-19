"""pkmodel is a Pharmokinetic modelling library.

It contains functionality for creating, solving, and visualising the solution
of Parmokinetic (PK) models

"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .model import Compartment, Model    # noqa
from .protocol import Dose, Protocol    # noqa
from .solution import Solution     # noqa
