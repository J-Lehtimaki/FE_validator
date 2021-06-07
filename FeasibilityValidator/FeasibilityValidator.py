# Author: Janne Lehtimäki
# Email: janne.lehtimaki@etteplan.com
# Company: Etteplan Finland Oy

# File description:
#   The sole purpose of this file is to run system call for single parameter-set
#   on program "ProFeValidator", and to interpret from that return value was the
#   case feasible or not. The class does not have nothing special functionality
#   other than that.

from .ENVfeasibilityValidator import VALIDATOR_EXE_PATH

# Param 1:
# []{} , where keys for boundary lattice coords paths are "pr", "pin", "thread", "fea"
#        an 
class FeasibilityValidator:
    def __init__(self):
        self._argList = []  # arguments for ProFeValidator
        
