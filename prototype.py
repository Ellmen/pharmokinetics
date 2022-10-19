import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

therapeutic_min=1 #TODO: Remove when class defining these is up and running
therapeutic_max=3

def dose(t, Xs):
    dosage = 0
    for X in Xs:
        if t > X[0] and t < X[1]:
            dosage += X[2]
    return dosage


def rhs(t, y, Q_p1, V_c, V_p1, CL, Xs):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, Xs) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'Xs': [[0,1,6]],
}

model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'Xs': [[0,0.001,4000],[0.5,0.501,2000]], #figure out why the second spike does not get plotted
}

t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0.0, 0.0])

fig = plt.figure()
for model in [model1_args, model2_args]:
    args = [
        model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['Xs']
    ]
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )
    plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')
    if np.max(sol.y) > therapeutic_max:
        print('Drug concentration of ' + model['name'] + ' exceeds toxic threshold, use lighter dosing')

[plt.axhline(y=i, linestyle='--') for i in [therapeutic_min,therapeutic_max]]
plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.savefig('output.png') #Change .plot into .savefig for the VM to run it