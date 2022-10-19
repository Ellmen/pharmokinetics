[![Python application](https://github.com/Ellmen/pharmokinetics/actions/workflows/python-app.yml/badge.svg)](https://github.com/Ellmen/pharmokinetics/actions/workflows/python-app.yml)
[![Documentation Status](https://readthedocs.org/projects/pharmokinetics/badge/?version=latest)](https://pharmokinetics.readthedocs.io/en/latest/?badge=latest)

# 2022-software-engineering-projects-pk
By Isaac Ellmen (Ellmen), Leonard Lee (XX) & Raman van Wee (Ramanspec) on 21 Oct 2022

This project describes drug delivery to a patient using a pharmacokinetic (pk) model. The body is modeled as consisting of various homogenous compartments which drug exchange occurring between them. Users are flexible in terms of the drug dosing protocol (continuous or instanenous), the model used (intravenous bolus or subcateneous) and the number of peripheral components (0 or more). The amount of drug in each compartment is modeled over time and can be visualized and compared with the therapeutic window.

Future extensions of this model may include incorporation of a pharmacodynamic (pd) model to describe the interactions of the drug with the body.

## Installation

```
pip install -r requirements.txt
pip install -e .
```
