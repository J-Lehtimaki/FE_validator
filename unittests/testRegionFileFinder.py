import unittest
import json

from RegionFileFinder.RegionFileFinder import RegionFileFinder
from .ENVunittest import \
    ABSPATH_GROUPS_JSONDUMP, \
    TEST_ROOT_DIR, \
    TEST_SAMPLE_ROOT_DIR, \
    TEST_ID_RANGE, \
    ABSPATH_MAJVER_JSONDUMP

class RegionFileFinderTestCase(unittest.TestCase):
    def setUp(self):
        self._RegFileFinder = RegionFileFinder(TEST_SAMPLE_ROOT_DIR)

    # Test that every major ID can be found in the test folder
    # and that the type of id is string
    def testMajorVersionsFound(self):
        majorVersions = self._RegFileFinder.getMajorVersionsFound()
        for i in range(TEST_ID_RANGE["begin"], TEST_ID_RANGE["end"]):
            self.assertTrue(str(i) in majorVersions)
    
    def testFindPins(self):
        a = self._RegFileFinder.findPinFiles()

    def testFindThreadFiles(self):
        a = self._RegFileFinder.findThreadFiles()

    def testFindPRFiles(self):
        a = self._RegFileFinder.findPRFiles()

    def testFindFEAresultFiles(self):
        a = self._RegFileFinder.findFEAresultFiles()

    def testGetMajorVersionDict(self):
        a = self._RegFileFinder.findPinFiles()
        b = self._RegFileFinder.findThreadFiles()
        c = self._RegFileFinder.findPRFiles()
        d = self._RegFileFinder.findFEAresultFiles()

        e = self._RegFileFinder.getMajorVersionDict()

        # Eyeball the results, all good
        with open(ABSPATH_MAJVER_JSONDUMP, 'w') as outfile:
            json.dump(e, outfile, indent=2)
        
    def testGroupFileLists(self):
        a = self._RegFileFinder.findPinFiles()
        b = self._RegFileFinder.findThreadFiles()
        c = self._RegFileFinder.findPRFiles()
        d = self._RegFileFinder.findFEAresultFiles()

        e = self._RegFileFinder.groupIDfileLists()

        # Again eyeball the results in the json file produced
        with open(ABSPATH_GROUPS_JSONDUMP, 'w') as outfile:
            json.dump(e, outfile, indent=2)
