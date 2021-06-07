# Author: Janne Lehtimäki
# Email:  janne.lehtimaki@etteplan.com
# Company: Etteplan Finland Oy

# File Description:
#   The purpose of this file is to provide class that can traverse through
#   filesystem to find the solutions that were completely created during
#   sample generation with nTopCL. (RockerArm W16)
#  
#   Details:
#   The sample generation was done with syscalls, and timeout was set to be 2hours.
#   This means that some samples were only partially generated.
#

import os
import glob

from .ENVregionFileFinder import \
    FEA_BOUNDARY_DESCRIPTORS, \
    FEA_BOUNDARY_DESCRIPTORS_FTYPE, \
    FEA_RESULT_DESCR_FTYPE, \
    FEA_RESULT_DESCR

class RegionFileFinder:
    def __init__(self, pathSampleRoot):
        self._searchPath = pathSampleRoot
        self._majIDList = self.getMajorVersionsFound()
        self._idDict = {}

        self._foundPinFiles = []
        self._foundThreadFiles = []
        self._foundPRFiles = []
        self._foundFEAresultFiles = []

        self.initiateMajorVersionDict()

    def getMajorVersionDict(self): return self._idDict

    def getMajorVersionsFound(self):
        retVal = []
        majVersionDirNames = glob.glob(os.path.join(self._searchPath, '*/'))
        for dName in majVersionDirNames:
            retVal.append(dName.split("\\")[-2])
        return retVal

    def initiateMajorVersionDict(self):
        for id in self._majIDList:
            self._idDict[id] = []

    def findFilesAndGroupToMajID(self):
        self.findFEAresultFiles()
        self.findPinFiles()
        self.findThreadFiles()
        self.findPRFiles()

    # For each major id, initializes all pin boundary files found
    def findPinFiles(self):
        self._foundPinFiles.clear()     # Prevent duplicates
        pinFileSearch = os.path.join(self._searchPath, '**/*pin*')
        for f in glob.iglob(pinFileSearch, recursive=True):
            self._foundPinFiles.append(f)
            id = f.split('\\')[-1].split('_')[1]
            self._idDict[id].append(f)
        return self._foundPinFiles

    # For each major id, initializes all thread boundary files found
    def findThreadFiles(self):
        self._foundThreadFiles.clear()  # Prevent duplicates
        threadFileSearch = os.path.join(self._searchPath, '**/*thread*')
        for f in glob.iglob(threadFileSearch, recursive=True):
            self._foundThreadFiles.append(f)
            id = f.split('\\')[-1].split('_')[1]
            self._idDict[id].append(f)
        return self._foundThreadFiles

    # For each major id, initializes all 
    # pr boundary files found
    def findPRFiles(self):
        self._foundPRFiles.clear()  # Prevent duplicates
        prFileSearch = os.path.join(self._searchPath, '**/*pr*')
        for f in glob.iglob(prFileSearch, recursive=True):
            self._foundPRFiles.append(f)
            id = f.split('\\')[-1].split('_')[1]
            self._idDict[id].append(f)
        return self._foundPRFiles

    # For each major id, initializes all fea boundary files found
    def findFEAresultFiles(self):
        self._foundFEAresultFiles.clear()   # Prevent duplicates
        feaFileSearch = os.path.join(self._searchPath,'**/*fea*.csv')
        for f in glob.iglob(feaFileSearch, recursive=True):
            self._foundFEAresultFiles.append(f)
            id = f.split('\\')[-1].split('_')[1]
            self._idDict[id].append(f)
        return self._foundFEAresultFiles

    def groupIDfileLists(self):
        groupIDs = {}
        # Create keys for all majverid_material_threshold -versions that has some
        # files generated for the sample in consideration. No need to be fully healthy
        # group at this stage
        for key in self._idDict:
            for path in self._idDict[key]:
                temp = path.strip('.csv').split('\\')[-1].split('_')
                groupID = '_'.join([temp[1],temp[2],temp[3]]) # majverid_material_threshold
                groupIDs[groupID] = []

        # Now append the groupID's that were found to include all the files that
        # have that ID
        for key in self._idDict:
            for path in self._idDict[key]:
                temp = path.strip('.csv').split('\\')[-1].split('_')
                groupID = '_'.join([temp[1],temp[2],temp[3]]) # majverid_material_threshold
                groupIDs[groupID].append(path)

        return groupIDs

