import unittest
import pkmodel as pk


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        s = pk.Solution(models=[], therapeutic_min=0, therapeutic_max=1)
        self.assertEqual(s.therapeutic_min, 0)

