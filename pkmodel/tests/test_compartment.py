import unittest
import pkmodel as pk

class CompartmentTest(unittest.TestCase):
    """Tests the compartment class"""
    
    def test_create_compartment(self):
        c = pk.Compartment(5, 5)
        self.assertEqual(c.rate, 5)
        self.assertEqual(c.volume, 5)

if __name__ == "__main__":
    unittest.main()