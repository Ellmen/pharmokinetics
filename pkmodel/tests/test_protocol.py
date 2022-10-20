import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        dosing_strategy = [pk.SpikeDose(8,1), pk.SpikeDose(6, 2)]
        p = pk.Protocol(dosing_strategy)
        self.assertEqual(p.dosing_strategy, dosing_strategy)
        
    def test_invalid_protocols(self):
        with self.assertRaises(TypeError):
            pk.Protocol("dose")
        with self.assertRaises(TypeError):
            pk.Protocol(["dose"])
        with self.assertRaises(ValueError):
            pk.Protocol(dosing_strategy=[])

if __name__ == "__main__":
    unittest.main()
