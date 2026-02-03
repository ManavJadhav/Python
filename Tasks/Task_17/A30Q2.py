######################################################################################################
# Program Name     : CountFileWords
# Input            : File name (command line argument)
# Output           : Displays total number of words in the file
# Description      : Counts the total number of words present in a text file
#                    using file handling and command line arguments.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import sys
import os


def CountWords(FileName) :

    Result = os.path.exists(FileName)
    if Result == False:
        print("There is no such file in the current directory")
        return
    
    Count = 0

    fobj = open(FileName,"r")

    for line in fobj:
        words = line.split()
        for word in words:
            Count += 1

    fobj.close()
                
    return Count


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
            Ret = CountWords(sys.argv[1])
            print("Total number of words are : ",Ret)
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)

if __name__ == "__main__":
    main()