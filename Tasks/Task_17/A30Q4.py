######################################################################################################
# Program Name     : CopyFileContent
# Input            : Source file name and destination file name
#                    (command line arguments)
# Output           : Creates destination file and copies content into it
# Description      : Copies contents of one file into another file using
#                    file handling and command line arguments.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import sys
import os

def CopyFileContent(FileName1,FileName2):

    Result = os.path.exists(FileName1)
    if Result == False:
        print("There is no such file in the current directory")
        return
    
    fobj1 = open(FileName1,"r")

    fobj2 = open(FileName2,"w")
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
    
    if(len(sys.argv) == 3):
        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This application is used to perform  FileIO")

        elif((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Use the given script as ")
            print("ProgramName.py Argument1 Argument2")   
            print("Argument 1 : First_FileName ")
            print("Argument 2 : Second_FileName ")
        else:
            CopyFileContent(sys.argv[1],sys.argv[2])
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)

if __name__ == "__main__":
    main()