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
import time

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
    Ret = ChkDirExist(DirName)
    if(Ret == False):
        sys.exit(1)
    

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

    Border = "-" * 50
    print(Border)
    print("------------ Directory Checksum Automation -----------")
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H")):
            print("This script is used to:")
            print("Calculate checksum of all files in a directory recursively")

        elif((sys.argv[1]== "--u") or (sys.argv[1]== "--U")):
            print("Usage:")
            print("ScriptName.py DirectoryName TimeInterval")
            print("DirectoryName     : Enter the name of directory")
            print("TimeInterval      : Time in minutes for periodic execution")

        else:
            print("Invalid option")
            print("Use --h or --u for help")

    elif(len(sys.argv) == 3 ):

        # Filter
        try:
            interval = int(sys.argv[2])
            if interval <= 0:
                raise ValueError
        except ValueError:
            print("TimeInterval must be a positive integer (minutes)")
            return

        print("Directory Name :", sys.argv[1])
        print("Time interval  :", interval, "minutes")

        schedule.every(interval).minutes.do(DirectoryChecksum, sys.argv[1])

        print("Directory Checksum Automation started at:", time.ctime())
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
    print("--------- Thank you for using this script ---------")
    print(Border)

# Entry point
if __name__ == "__main__":
    main()


