# Author: Janne Lehtimäki

# File description:
#   The sole purpose of this file is to run system call for single parameter-set
#   on program "ProFeValidator", and to interpret from that return value was the
#   case feasible or not. The class does not have nothing special functionality
#   other than that.

from .ENVfeasibilityValidator import VALIDATOR_EXE_PATH

import os

class FeasibilityValidator:
    def __init__(self,CppFErunnerEXEpath):
        self._exePath = os.path.normpath(CppFErunnerEXEpath)

    # Runs systemcall on CppFErunner to check case feasibility.
    # return <bool>:
    #   - True when case was feasible
    #   - False when not
    def isFeasible(self,
                designLimitStress,
                pathFEA,
                pathPin,
                pathThread,
                pathPR,
                pathExportSubtractRegionNodeStress,
                pathExportSubtractRegionGeneralStressData):
        args = "{a} {b} {c} {d} {e} {f} {g} {h}".format(
            a=self._exePath,
            b=str(designLimitStress),
            c=os.path.normpath(pathFEA),
            d=os.path.normpath(pathPin),
            e=os.path.normpath(pathThread),
            f=os.path.normpath(pathPR),
            g=os.path.normpath(pathExportSubtractRegionNodeStress),
            h=os.path.normpath(pathExportSubtractRegionGeneralStressData)
        )

        if(os.system(args) == 0):
            return True
        return False

    # Runs systemcall on CppFErunner to check case feasibility.
    # return param1 with boolean field "feasibility":
    #   - True when case was feasible
    #   - False when not
    def isFeasibleFromMap(self, mapSingleKey):
        # There can be only one key in the param1, else this fails
        retval = mapSingleKey
        retval["feasible"] = False  # Default is fail
        if(len(mapSingleKey) != 2):
            return retval
        for key in mapSingleKey:
            args = "{a} {b} {c} {d} {e} {f} {g} {h}".format(
                a=self._exePath,
                b=str(mapSingleKey[key][6]),
                c=os.path.normpath(mapSingleKey[key][0]),
                d=os.path.normpath(mapSingleKey[key][1]),
                e=os.path.normpath(mapSingleKey[key][2]),
                f=os.path.normpath(mapSingleKey[key][3]),
                g=os.path.normpath(mapSingleKey[key][4]),
                h=os.path.normpath(mapSingleKey[key][5])
            )
            if(os.system(args) == 0):
                retval["feasible"] = True
            return retval