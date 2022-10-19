#
# Solution class
#
from scipy.integrate import solve_ivp as ODE_solver

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, models, protocols):
        self.models = models
        self.protocols = protocols

    # Implement method that iterates over the permuations of models and 
    # protocols and stores the solution
    def solve(self):
        pass

    # Implement method that plots the solutions via matplotlib
    def plot(self):
        pass

    # Implement method that saves the plots to a specified file path
    def save_plot(self, filepath):
        pass
