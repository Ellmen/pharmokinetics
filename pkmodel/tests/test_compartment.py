import unittest
import pkmodel as pk

class CompartmentTest(unittest.TestCase):
    """Tests the compartment class"""
    
    def test_create_peripheral(self):
        c = pk.Compartment("peripheral", 5, 5)
        self.assertEqual(c.c_type, "peripheral")
        self.assertEqual(c.rate, 5)
        self.assertEqual(c.volume, 5)

    def test_create_dosing(self):
        c = pk.Compartment("dosing", 5, 5)
        self.assertEqual(c.volume, 0)
    
    def test_invalid_compartment(self):
        with self.assertRaises(ValueError):
            c = pk.Compartment("sdf", 1, 4)

if __name__ == "__main__":
    unittest.main()