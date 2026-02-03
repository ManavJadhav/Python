######################################################################################################
# Program Name     : CopyFileUsingCommandLine
# Input            : Source file name (command line argument)
# Output           : Creates Demo.txt and copies data into it
# Description      : Copies contents of a file into another file using
#                    command line arguments and buffer-based file I/O.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import sys
import os

def CopyFileContent(FileName):

    Result = os.path.exists(FileName)
    if Result == False:
        print("There is no such file in the current directory")
        return
    
    fobj1 = open(FileName,"r")

    fobj2 = open("Demo.txt","w")
    print("Demo.txt created successfully")


    Buffer = fobj1.read(1024)

    while(len(Buffer) > 0):
        fobj2.write(Buffer)
        Buffer = fobj1.read(1024)

    print("Data copied successfully")

    fobj1.close()
    fobj2.close()


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
            CopyFileContent(sys.argv[1])
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)

if __name__ == "__main__":
    main()