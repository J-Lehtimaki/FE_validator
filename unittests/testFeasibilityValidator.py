import unittest

from FeasibilityValidator.FeasibilityValidator import FeasibilityValidator

class FeasibilityValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self._FeasValidator = FeasibilityValidator()

    # Clear this
    def testDummyTwo(self):
        self.assertEqual(2,2)
