#=====================================================================================================
# Program Name     : DirectoryCopyAutomation
# Input            : Source directory, destination directory, time interval (CLI arguments)
# Output           : Copies files and subdirectories while preserving directory structure
# Description      : Periodically traverses a source directory and copies all files and
#                    subdirectories into a destination directory using os.walk and shutil.
# Author           : Manav Mahadev Jadhav
# Date             : 10/02/2026
#=====================================================================================================

import sys
import os
import time
import shutil

#---------------------- Dependency Check ----------------------
try:
    import schedule
except ImportError:
    print("Required module 'schedule' not found.")
    print("Install it using: pip install schedule")
    sys.exit(1)

#------------------------------------------------------------------------
# Function    : ChkDirExist
# Description : Checks whether the given path exists and is a directory
#------------------------------------------------------------------------
def ChkDirExist(Dname):
    Border = "-" * 90

    if not os.path.exists(Dname):
        print("There is no such directory")
        print(Border)
        return False

    if not os.path.isdir(Dname):
        print("It is not a directory")
        print(Border)
        return False

    return True

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
    
    copied_files = []
    print(Border)
    if not os.path.exists(NewDirName):
        os.mkdir(NewDirName)
        print(f"{NewDirName} created succesfully")
    print(Border+"\n")

    
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

            shutil.copy2(src_file,dst_file)
            copied_files.append(dst_file)
    print(Border)
    print(f"All files of {ExistDirName} gets copied to {NewDirName} successfully")
    print(Border)

#-------------------------------------
# Function    : main
# Description : Driver code
#-------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("------------ Directory Copy Automation -----------")
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This script is used to:")
            print("Copy files from source folder to destination folder")

        elif((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Usage:")
            print("ScriptName.py SourceDirectory DestinationDirectory TimeInterval")
            print("SourceDirectory       : Name of Exsisting Directory")
            print("DestinationDirectory  : Name of Destination Directory")
            print("TimeInterval          : Time in minutes for periodic execution")

        else:
            print("Invalid option")
            print("Use --h or --u for help")

    elif(len(sys.argv) == 4 ):

        # Filter
        try:
            interval = int(sys.argv[3])
            if interval <= 0:
                raise ValueError
        except ValueError:
            print("TimeInterval must be a positive integer (minutes)")
            return

        print("SourceDirectory Name :", sys.argv[1])
        print("DestinationDirectory Name :", sys.argv[2])
        print("Time interval  :", interval, "minutes")

        schedule.every(interval).minutes.do(DirectoryCopy, sys.argv[1], sys.argv[2])

        print("Directory Copy Automation started at:", time.ctime())
        print("Press Ctrl + C to stop the execution")

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nAutomation stopped by user")

    else:
        print("Invalid number of command line arguments")
        print("Use --h or --u for help")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

# Entry point
if __name__ == "__main__":
    main()

