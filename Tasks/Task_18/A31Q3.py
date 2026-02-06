#=====================================================================================================
# Program Name     : DirectoryCopy
# Input            : Existing directory name, New directory name (command line arguments)
# Output           : Copies all files and sub-directories into a new directory
# Description      : Recursively copies the contents of one directory into another
#                    directory using os.walk and binary file handling.
# Author           : Manav Mahadev Jadhav
# Date             : 04/02/2026
#=====================================================================================================

import sys
import os


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

#------------------------------------------------------------------------------------------------------------------------------
# Function    : DirectoryCopy
# Description : Copies all files and subdirectories from source directory to destination directory while preserving structure
#------------------------------------------------------------------------------------------------------------------------------

#                   Demo            Temp
def DirectoryCopy(ExistDirName ,NewDirName ):
    Border = "-"*90
    Ret = ChkDirExist(ExistDirName)
    if(Ret == False):
        return
    
    if not os.path.exists(NewDirName):
        os.mkdir(NewDirName)
        print(f"{NewDirName} created succesfully")

    
    for DirectoryName , SubFolderName , FileName in os.walk(ExistDirName):
        
        # For Nested Folder
        # Demo directory contains-> Hello directory

        relative_path = os.path.relpath(DirectoryName, ExistDirName)
         
        # For first iteration relative_path = .
        # For second iteration relative_path = Hello
        

        dest_dir = os.path.join(NewDirName, relative_path)
        # For first iteration dest_dir = Temp/.                 (same as Temp)
        # For second iteration dest_dir = Temp/Hello
 

        if (os.path.exists(dest_dir) == False):
            os.mkdir(dest_dir)
            # os.mkdir works here because os.walk visits parent directories first

        # For Files
        for fname in FileName :
            src_file= os.path.join(DirectoryName,fname)
            # For first iteration src_file = Demo/ABC.py
            # src_file = Demo/Hello/XYZ.py
            
            dst_file= os.path.join(dest_dir,fname)
           # For first iteration dst_file = Temp/./ABC.py       (same as Temp/ABC.py)
           #  For second iteration dst_file = Temp/Hello/XYZ.py

            fobj1 = open(src_file,"rb")
            fobj2 = open(dst_file,"wb")
            
            data = fobj1.read()
            fobj2.write(data)

            fobj1.close()
            fobj2.close()

#-------------------------------------
#  Function    :       main
#  Description :       Driver Code 
#-------------------------------------

def main():

    Border = "-"*90
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This application is used to copy all files from old directory to new directory")
            print(Border)
            return

        if((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Use the given script as ")
            print(Border)
            print("ScriptName.py Argument1 Argument2")   
            print("Argument 1 : Existing Directory Name  ")
            print("Argument 2 : New Directory Name  ")
            print(Border)
            return
    
    if(len(sys.argv) == 3 ):
        DirectoryCopy(sys.argv[1],sys.argv[2])
        
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")
        print(Border)
            

    

if __name__ == "__main__":
    main()