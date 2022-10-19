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
        p = pk.Protocol(dosing_strategy=[])
        self.assertEqual(p.dosing_strategy, [])

