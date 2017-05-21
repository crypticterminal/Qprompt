##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import qprompt

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

GENFILE = "generated_file.txt"

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def gen_file():
    with open(GENFILE, "w") as fo:
        fo.write("just a test")

def del_file():
    os.remove(GENFILE)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    menu = qprompt.Menu()
    menu.add("g", "Generate file", gen_file)
    menu.add("d", "Delete file", del_file)
    menu.main(loop=True)
