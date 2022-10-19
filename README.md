[![Python application](https://github.com/Ellmen/pharmokinetics/actions/workflows/python-app.yml/badge.svg)](https://github.com/Ellmen/pharmokinetics/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/github/Ellmen/pharmokinetics/branch/master/graph/badge.svg?token=JFMPK5650Q)](https://codecov.io/github/Ellmen/pharmokinetics)
[![Documentation Status](https://readthedocs.org/projects/pharmokinetics/badge/?version=latest)](https://pharmokinetics.readthedocs.io/en/latest/?badge=latest)

# 2022-software-engineering-projects-pk
By Isaac Ellmen (Ellmen), Leonard Lee (leonard-lenny-lee) & Raman van Wee (Ramanspec). Project development ceased on 21 Oct 2022

This project describes drug delivery to a patient using a pharmacokinetic (pk) model. The body is modeled as consisting of separate homogenous compartments with drug exchange occurring between them through the exchange of liquid. In its most simple form, a drug dose is administered directly to the central compartment where it performs its function and from which is it is cleared. More complex models include one ore more peripheral components around the central component or an initial compartment from which the drug is absorbed into the central compartment. The amount of drug in each compartment is modeled over time and can be visualized and compared with the therapeutic window. See [Wikipedia](https://en.wikipedia.org/wiki/Pharmacokinetics) for more information.

The system of equations for a model with subcutaneous dosing and i peripheral compartments is given by:


$$
{dq_0 \over dt} = {Dose(t)-k_aq_0} 
$$

$$
{dq_c \over dt} = {k_a q_0 - {q_c \over V_c}  CL - Q_{p1}({q_c \over V_c} - {q_{p1} \over V_{p1}}) ... - Q_{pi}({q_c \over V_c} - {q_{pi} \over V_{pi}})}
$$

$$
{dq_{p1} \over dt}={Q_{p1}({q_c \over V_c} - {q_{p1} \over V_{pi}})}
$$

$$
{.}
$$

$$
{.}
$$

$$
{.}
$$

$$
{dq_{pi} \over dt}={Q_{pi}({q_c \over V_c} - {q_{pi} \over V_{pi}})}
$$

where $q_0$, $q_c$ & $q_i$ are the the masses of the drug in the initial, the central, and the peripheral compartments (in ng), respectively. $Dose(t)$ describes the drug administration profile, while $V_c$ & $V_{pi}$ are the volumes of the central and peripheral compartments (in mL). Lastly, $CL$, $k_a$ & $Q_{pi}$ are the rates of clearance out of the central compartment in the external environment (in mL/h), the absorption rate from the initial compartment into the central compartment (in /h), and the transition rate between the central compartment and the ith peripheral compartment (in mL/h), respectively. When the drug is administered intravenously (direcly into the central compartment) $k_aq_0 = Dose(t)$.

The model consists of three classes: (1) [Model](https://github.com/Ellmen/pharmokinetics/blob/master/pkmodel/model.py) to define the method of drug administration used (intravenous bolus or subcateneous) and the number of peripheral components (0 or more), (2) [Protocol](https://github.com/Ellmen/pharmokinetics/blob/master/pkmodel/protocol.py) to specify the dosing protocol (continuous or instaneous), and (3) [Solution](https://github.com/Ellmen/pharmokinetics/blob/master/pkmodel/solution.py) to solve the resulting system of differential equations and generate plots. The used model and protocol can be chosen independently and compared, see example plot below.

![image](https://user-images.githubusercontent.com/115243223/196722164-fa55ceed-6599-4c8f-8a1d-b725d6d1c263.png)

#TODO: update figure with eventual plot

## Roadmap
Future extensions of this model may include incorporation of a pharmacodynamic (pd) model to describe the varying interactions of different drugs with the body. Moreover, the drug administration protocol may be made dependent on current drug levels in the body to facilitated automated administration.

## Installation

```
pip install -r requirements.txt
pip install -e .
```
