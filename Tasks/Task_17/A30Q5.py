######################################################################################################
# Program Name     : CheckWordPresence
# Input            : File name and word (command line arguments)
# Output           : Displays whether the specified word is present in the file
# Description      : Checks the presence of a given word in a text file
#                    using file handling and command line arguments.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import sys
import os

def WordCheck(FileName ,StrA) :

    Result = os.path.exists(FileName)
    if Result == False:
        print("There is no such file in the current directory")
        return
    
    flag = False

    fobj = open(FileName,"r")

    for line in fobj:
        words = line.split()
        for word in words:
            if word == StrA:
                flag = True

    fobj.close()

    return flag
                


def main():

    Border = "-"*50
    print(Border)
    
    if(len(sys.argv) == 3):
        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This application is used to perform  FileIO")

        elif((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Use the given script as ")
            print("ProgramName.py Argument1  Argument2")   
            print("Argument 1 : First_FileName ")
            print("Argument 2 : String ")
        else:
            Ret = WordCheck(sys.argv[1],sys.argv[2])
            if(Ret == True):
                print(f"Word {sys.argv[2]} is present in the file")
            else:
                print(f"Word {sys.argv[2]} is NOT present in the file")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)

if __name__ == "__main__":
    main()