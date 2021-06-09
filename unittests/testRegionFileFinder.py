import unittest
import json

from RegionFileFinder.RegionFileFinder import RegionFileFinder
from .ENVunittest import \
    ABSPATH_GROUPS_JSONDUMP, \
    TEST_ROOT_DIR, \
    TEST_SAMPLE_SEARCH_PATH, \
    TEST_SAMPLE_ROOT_DIR, \
    TEST_ID_RANGE, \
    ABSPATH_MAJVER_JSONDUMP, \
    ABSPATH_FILTERED_GROUPS_JSONDUMP, \
    ABSPATH_NOMATERIAL_CPP_RUNNER_GROUPS_JSONDUMP, \
    ABSPATH_CPP_RUNNER_COMPLETE_JSONDUMP

class RegionFileFinderTestCase(unittest.TestCase):
    def setUp(self):
        self._RegFileFinder = RegionFileFinder(
                                TEST_SAMPLE_SEARCH_PATH,
                                TEST_SAMPLE_ROOT_DIR
                                )
        self._RegFileFinder.findFilesAndGroupToMajID()

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
        b = self._RegFileFinder.getMajorVersionDict()
        # Eyeball the results, all good
        with open(ABSPATH_MAJVER_JSONDUMP, 'w') as outfile:
            json.dump(b, outfile, indent=2)
        
    def testGroupFileLists(self):
        b = self._RegFileFinder.groupIDfileLists()
        # Again eyeball the results in the json file produced
        with open(ABSPATH_GROUPS_JSONDUMP, 'w') as outfile:
            json.dump(b, outfile, indent=2)

    def testFilterIncompleteFileLists(self):
        a = self._RegFileFinder.filterIncompleteIDfileLists()
        with open(ABSPATH_FILTERED_GROUPS_JSONDUMP, 'w') as outfile:
            json.dump(a, outfile, indent=2)

    def testCppFErunnerNoMaterialParameters(self):
        a = self._RegFileFinder.addCppFerunnerExportPaths()
        with open(ABSPATH_NOMATERIAL_CPP_RUNNER_GROUPS_JSONDUMP, 'w') as outfile:
            json.dump(a, outfile, indent=2)

    def testCppFErunnerParameters(self):
        designLimitStresses = {"IN718":200000000, "316L":80000000}
        a = self._RegFileFinder.getCompleteFErunnerParameterSet(designLimitStresses)
        with open(ABSPATH_CPP_RUNNER_COMPLETE_JSONDUMP, 'w') as outfile:
            json.dump(a, outfile, indent=2)
        