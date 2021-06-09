# Author: Janne Lehtimäki

#                * * * FEASIBLE SOLUTION FINDER * * *                 #
# Desription:
#  Performs stage 2. in the multi-objective optimization, which is
#  extracting the feasible solutions from all solutions. Here this is
#  achieved by using the design stress limits as constraints for
#  feasibility. At this stage this is the only constraint there is.
#    (V1.0): Searches solutions only for one case. Further versions could
#  do multiple cases by iterating safety-factor, and dumping each case to
#  separate JSON-file.
# Guide:
#  Tweak design limit stress in ENV.ENVIRONMENT to 

from RegionFileFinder.RegionFileFinder import RegionFileFinder
from FeasibilityValidator.FeasibilityValidator import FeasibilityValidator

from ENV.ENVIRONMENT import \
    DIR_SAMPLE_EXPORT, \
    DIR_SAMPLE_FILE_SEARCH, \
    DESIGN_LIMIT_STRESSES, \
    DIR_CASES_FEASIBLE_SOLUTIONS_JSON, \
    VALIDATOR_EXE_PATH

import concurrent.futures
import os
import json

def createCaseID(materialDict):
    temp = []
    for key in materialDict:
        temp.append(key)
        temp.append(str(materialDict[key]))
    return "_".join(temp)

def createJsonCasePath(dirFeasibleSols, caseID):
    filename = ".".join([caseID, "json"])
    abspath = os.path.join(dirFeasibleSols, filename)
    return abspath

# Creates the folder for the cases if it doesn't already exist
def createFeasibleSolutionFolder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

def main():
    # Step 1: Setup all necessary parameters and classes for iteration
    createFeasibleSolutionFolder(DIR_CASES_FEASIBLE_SOLUTIONS_JSON)
    caseID = createCaseID(DESIGN_LIMIT_STRESSES)  # filename for json dump
    feasibleSolutions = {}

    pathFeasibleSolutions = createJsonCasePath(
        DIR_CASES_FEASIBLE_SOLUTIONS_JSON, caseID
    )
    validator = FeasibilityValidator(VALIDATOR_EXE_PATH)
    regionFileHandler = RegionFileFinder(
        DIR_SAMPLE_FILE_SEARCH,
        DIR_SAMPLE_EXPORT
    )
    regionFileHandler.findFilesAndGroupToMajID()
    CppFErunnerParameters = \
        regionFileHandler.getCompleteFErunnerParameterSet(
            DESIGN_LIMIT_STRESSES
        )

    # Step 2: Speed things up with threadpoolexecutor
    # For one sample ~20 seconds to process (meshsize ~200000)
    # There are plenty samples, so good idea to speed things up
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(validator.isFeasibleFromMap,
            {p:CppFErunnerParameters[p]}
        )
            for p in CppFErunnerParameters
        ]
        for f in concurrent.futures.as_completed(results):
            res = f.result()
            if(res["feasible"]):
                del res["feasible"]
                for solutionID in res:
                    feasibleSolutions[solutionID] = res[solutionID]

    with open(pathFeasibleSolutions, 'w') as outfile:
        json.dump(feasibleSolutions, outfile, indent=2)

if __name__ == '__main__':
    main()
