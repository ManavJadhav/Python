######################################################################################################
# Program Name     : CompareFileChecksum
# Input            : Two file names (command line arguments)
# Output           : Displays Success if both files are identical,
#                    otherwise displays Failure
# Description      : Compares two files by calculating and matching their
#                    MD5 checksums using file handling and hashing techniques.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import sys
import os
import hashlib

def CalculateChecksum(Filename):
    fobj = open(Filename,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def CompareFile(FileName1 ,FileName2) :

    Result = os.path.exists(FileName1) and os.path.exists(FileName2)
    if Result == False:
        print("There is no such file in the current directory")
        return

    Ret1 = CalculateChecksum(FileName1)
    Ret2 = CalculateChecksum(FileName2)


    if(Ret1 == Ret2):
        print("Success")
    else:
        print("Failure")


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
            print("Argument 2 : Second_FileName ")
        else:
            CompareFile(sys.argv[1],sys.argv[2])
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)

if __name__ == "__main__":
    main()