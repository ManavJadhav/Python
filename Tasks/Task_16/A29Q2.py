######################################################################################################
# Program Name     : DisplayFileContent
# Input            : File name (string)
# Output           : Displays contents of the specified file
# Description      : Opens an existing file and reads its complete content
#                    using file handling operations.
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import os

def DisplayFileContent(FileName):

    Result = os.path.exists(FileName)
    if Result == False:
        print("There is no such file in the current directory")
        return
    
    fobj = open(FileName,"r")

    Data = fobj.read()

    print(Data)

    fobj.close()


def main():

    print("Enter the name of the file : ")
    fname = input()

    DisplayFileContent(fname)

if __name__ == "__main__":
    main()