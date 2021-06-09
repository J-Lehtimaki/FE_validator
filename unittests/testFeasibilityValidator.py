import unittest
import os

from FeasibilityValidator.FeasibilityValidator import FeasibilityValidator
from FeasibilityValidator.ENVfeasibilityValidator import \
    VALIDATOR_EXE_PATH, \
    DESIGN_LIMIT_STRESS, \
    PATH_FEA, \
    PATH_PIN, \
    PATH_THREAD, \
    PATH_PR, \
    PATH_EXPORT_SUBT_REGION, \
    PATH_EXPORT_DATA_REGION

class FeasibilityValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self._FeasValidator = FeasibilityValidator()
        self._args = "{a} {b} {c} {d} {e} {f} {g} {h}".format(
            a=os.path.normpath(VALIDATOR_EXE_PATH),
            b=DESIGN_LIMIT_STRESS,
            c=os.path.normpath(PATH_FEA),
            d=os.path.normpath(PATH_PIN),
            e=os.path.normpath(PATH_THREAD),
            f=os.path.normpath(PATH_PR),
            g=os.path.normpath(PATH_EXPORT_SUBT_REGION),
            h=os.path.normpath(PATH_EXPORT_DATA_REGION),
        )

    def testSyscallCppValidator(self):
        cppRetval = os.system(self._args)
        self.assertEqual(0, cppRetval)  # OK when dlStress ~85MPa

    