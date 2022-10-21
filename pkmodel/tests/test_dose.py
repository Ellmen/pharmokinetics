import unittest
import pkmodel as pk

class TestDoses(unittest.TestCase):
    "Tests to Dose class and its children classes"

    def test_dose_create(self):
        from math import inf
        d1 = pk.Dose(1.4)
        self.assertEqual(d1.start, 0)
        self.assertEqual(d1.end, inf)
        self.assertEqual(d1.rate, 1.4)
        d2 = pk.Dose(4.5, 5, 10)
        self.assertEqual(d2.rate, 4.5)
        self.assertEqual(d2.start, 5)
        self.assertEqual(d2.end, 10)
        with self.assertRaises(TypeError):
            pk.Dose()

    def test_spike_dose(self):
        d = pk.SpikeDose(5, 3)
        self.assertEqual(d.start, 3)
        self.assertEqual(d.end, 3.01)
        self.assertEqual(d.rate, 500)
