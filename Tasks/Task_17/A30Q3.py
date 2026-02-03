######################################################################################################
# Program Name     : DisplayFileLineByLine
# Input            : File name (command line argument)
# Output           : Displays file contents line by line
# Description      : Reads and displays the contents of a text file
#                    line by line using file handling and command line arguments.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import sys
import os


def DisplayLineByLine(FileName) :

    Result = os.path.exists(FileName)
    if Result == False:
        print("There is no such file in the current directory")
        return
    
    Count = 0

    fobj = open(FileName,"r")

    for line in fobj:
        print(line,end="")

    fobj.close()

def main():

    Border = "-"*50
    print(Border)
    
    if(len(sys.argv) == 2):
        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This application is used to perform  FileIO")

        elif((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Use the given script as ")
            print("ProgramName.py Argument1 ")   
            print("Argument 1 : FileName ")
        else:
            DisplayLineByLine(sys.argv[1])
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)

if __name__ == "__main__":
    main()