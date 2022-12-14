# TODO: working example - incorporate into tests


from pkmodel import Compartment, Dose, SpikeDose, Model, Protocol, Solution


c1 = Compartment(rate=1.0, volume=1.0)
c2 = Compartment(rate=2.0, volume=1.0)


d1 = Dose(rate=6, start=0, end=1)
d2 = SpikeDose(volume=4, start=0)
d3 = SpikeDose(volume=2, start=0.5)
d4 = SpikeDose(volume=2, start=1.0)
p1 = Protocol(dosing_strategy=[d1])
p2 = Protocol(dosing_strategy=[d2,d3,d4])

m1 = Model(name='model1', volume=1.0, clearance_rate=1.0, peripherals=[c1, c2], protocol=p1)
m2 = Model(name='model2', dosing_rate=5, volume=1.0, clearance_rate=1.0, peripherals=[c1], protocol=p2)

models = [m1, m2]
s = Solution(models=models, therapeutic_min=1, therapeutic_max=3, time=1.5)

s.solve()
s.plot()
# s.save_plot()
