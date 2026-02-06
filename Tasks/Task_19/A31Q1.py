#=====================================================================================================
# Program Name     : DirectoryChecksum
# Input            : Directory name (command line argument)
# Output           : Displays checksum of each file in the directory
# Description      : Traverses a directory structure recursively and calculates
#                    MD5 checksum for each file using hashlib.
# Author           : Manav Mahadev Jadhav
# Date             : 04/02/2026
#=====================================================================================================

import sys
import os
import hashlib

#------------------------------------------------------------------------
# Function    : ChkDirExist
# Description : Checks whether the given path exists and is a directory
#------------------------------------------------------------------------

def ChkDirExist(Dname):
    Border = "-"*90
    Ret = False

    Ret = os.path.exists(Dname)
    if(Ret == False):
        print("There is no such directory")
        print(Border)
        return Ret
    
    Ret = os.path.isdir(Dname)
    if(Ret == False):
        print("It is not a directory")
        print(Border)
        return Ret
    
    return Ret

#------------------------------------------------------------------------
# Function    : CheckSumCalculate
# Description : Calculates MD5 checksum of a given file
#------------------------------------------------------------------------

def CheckSumCalculate(file_name):
    
    fobj = open(file_name,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

#------------------------------------------------------------------------
# Function    : DirectoryChecksum
# Description : Traverses directory and prints checksum of each file
#------------------------------------------------------------------------

def DirectoryChecksum(DirName):
    Border = "-"*90
    Ret = ChkDirExist(DirName)
    if(Ret == False):
        return
    

    for DirectoryName , SubFolderName , FileName in os.walk(DirName):
        
        for fname in FileName :
            fname = os.path.join(DirectoryName,fname)
            Ret = CheckSumCalculate(fname)
            print(f"CheckSum of {fname} is : ",Ret)
            
#-------------------------------------
#  Function    :       main
#  Description :       Driver Code 
#-------------------------------------

def main():

    Border = "-"*90
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This application is used to display checksum of all files")
            print(Border)
            return

        if((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Use the given script as ")
            print(Border)
            print("ScriptName.py Argument1 ")   
            print("Argument 1 : Directory Name ")
            print(Border)
            return
    
    if(len(sys.argv) == 2 ):
        DirectoryChecksum(sys.argv[1])
        
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")
        print(Border)
            

    

if __name__ == "__main__":
    main()