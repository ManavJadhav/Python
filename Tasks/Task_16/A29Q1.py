######################################################################################################
# Program Name     : CheckFileExistence
# Input            : File name (string)
# Output           : Displays whether the given file exists or not
# Description      : Checks the presence of a file in the current directory
#                    using os.path.exists().
# Author           : Manav Mahadev Jadhav
# Date             : 01/02/2026
######################################################################################################

import os

def ChkFileExist(FileName):

    Result = os.path.exists(FileName)
    if Result == True:
        print(f"{FileName} is present in the current directory")
    else:
        print("There is no such file in the current directory")


def main():

    print("Enter the name of the file : ")
    fname = input()

    ChkFileExist(fname)

if __name__ == "__main__":
    main()