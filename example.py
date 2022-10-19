# TODO: working example - incorporate into tests


from pkmodel import Compartment, Dose, Model, Protocol, Solution


c1 = Compartment(c_type="peripheral", rate=1.0, volume=1.0)
c2 = Compartment(c_type="peripheral", rate=2.0, volume=1.0)


d1 = Dose(rate=6, start=0, end=1)
d2 = Dose(rate=4000, start=0, end=0.001)
d3 = Dose(rate=2000, start=0.5, end=0.501)
p1 = Protocol(dosing_strategy=[d1])
p2 = Protocol(dosing_strategy=[d2,d3])

m1 = Model(name='model1', volume=1.0, clearance_rate=1.0, peripherals=[c1], protocol=p1)
# m2 = Model(name='model2', volume=1.0, clearance_rate=1.0, peripherals=[c2], protocol=p2)
m2 = Model(name='model2', volume=1.0, clearance_rate=1.0, peripherals=[c1, c2], protocol=p2)

# protocols = [p1, p2]
models = [m1, m2]
# s = Solution(models=models, protocols=protocols)
s = Solution(models=models, therapeutic_min=1, therapeutic_max=3)

s.solve()
s.plot()
# s.save_plot()
