import unittest
import numpy as np
import pkmodel as pk


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """

    def setUp(self):
        c1 = pk.Compartment(c_type="peripheral", rate=1.0, volume=1.0)
        c2 = pk.Compartment(c_type="peripheral", rate=2.0, volume=1.0)


        d1 = pk.Dose(rate=6, start=0, end=1)
        d2 = pk.SpikeDose(volume=4, start=0)
        d3 = pk.SpikeDose(volume=2, start=0.5)
        p1 = pk.Protocol(dosing_strategy=[d1])
        p2 = pk.Protocol(dosing_strategy=[d2,d3])

        m1 = pk.Model(name='model1', volume=1.0, clearance_rate=1.0, peripherals=[c1], protocol=p1)
        m2 = pk.Model(name='model2', volume=1.0, clearance_rate=1.0, peripherals=[c1, c2], protocol=p2)

        self.models = [m1, m2]

        # s.solve()
        # s.plot()
        # s.save_plot()

    def test_create(self):
        """
        Tests Solution creation.
        """
        s = pk.Solution(models=self.models, therapeutic_min=1, therapeutic_max=3)
        self.assertEqual(s.therapeutic_min, 1)

    def test_dose(self):
        s = pk.Solution(models=self.models, therapeutic_min=1, therapeutic_max=3)
        dosage = s._dose(t=0.5, protocol=self.models[0].protocol)
        self.assertEqual(dosage, 6)
        dosage = s._dose(t=1.5, protocol=self.models[0].protocol)
        self.assertEqual(dosage, 0)

    def test_rhs(self):
        s = pk.Solution(models=self.models, therapeutic_min=1, therapeutic_max=3)
        for model in s.models:
            y0 = np.array([0.0] + [0.0 for _ in model.peripherals])
            rhs = s._rhs(0.5, y0, model)
            # TODO: test for correctness
            self.assertEqual(len(y0), len(rhs))

    def test_solve(self):
        s = pk.Solution(models=self.models, therapeutic_min=1, therapeutic_max=3)
        self.assertEqual(s.solutions, {})
        s.solve()
        # TODO: test for correctness
        self.assertEqual(set(s.solutions.keys()), set([m.name for m in s.models]))

if __name__ == "__main__":
    unittest.main()
