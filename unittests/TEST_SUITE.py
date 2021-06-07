from .testRegionFileFinder import RegionFileFinderTestCase as RFF
from .testFeasibilityValidator import FeasibilityValidatorTestCase as FV

import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RFF("test_region_file_finder"))
    suite.addTest(FV("test_feasibility_validator"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestResult()
    runner.run(suite())
