import unittest
from unittest.mock import Mock
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        m = pk.Model(name="PK model", volume=1, clearance_rate=1, protocol=Mock())
        self.assertEqual(m.name, "PK model")

if __name__ == "__main__":
    unittest.main()