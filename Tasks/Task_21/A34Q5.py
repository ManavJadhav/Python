#=====================================================================================================
# Program Name     : DataShieldSystem
# Input            : --history SourceDirectory LogFileName
# Output           : Backup of new/modified files with zip archive and persistent history log
# Description      :
#   - Copies only new or modified files
#   - Creates compressed archive of backup folder
#   - Appends backup details to a single history log file
# Author           : Manav Mahadev Jadhav
# Date             : 26/02/2026
#=====================================================================================================

import sys
import os
import time
import shutil
import hashlib
import zipfile


#-----------------------------------------------------------------------------------------------------
# Function Name    : CreateLog
# Description      : Appends backup details into a persistent history log file.
# Parameters       :
#   FileName   -> Log file name
#   files      -> List of copied files
#   StartTime  -> Backup start time
#   zip_file   -> Generated zip file name
#-----------------------------------------------------------------------------------------------------
def CreateLog(FileName, files, StartTime, zip_file):

    Border = "-" * 50

    with open(FileName, "a") as fobj:

        fobj.write(Border + "\n")
        fobj.write("--------- Data Shield System ----------\n")
        fobj.write("Log created at : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n")

        fobj.write("Backup started at : " + StartTime + "\n")
        fobj.write(Border + "\n\n")

        fobj.write("Copied Files:\n")
        fobj.write(Border + "\n")

        for file in files:
            fobj.write(file + "\n")

        fobj.write("\n" + Border + "\n")
        fobj.write("Zip File Generated:\n")
        fobj.write(Border + "\n")
        fobj.write(zip_file + "\n")
        fobj.write(Border + "\n")

        fobj.write("Backup completed at : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n\n")


#-----------------------------------------------------------------------------------------------------
# Function Name    : make_zip
# Description      : Creates zip archive of backup directory.
# Parameters       :
#   folder -> Folder to compress
# Returns          :
#   Generated zip file name
#-----------------------------------------------------------------------------------------------------
def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = f"{folder}_{timestamp}.zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zobj:
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)
                zobj.write(full_path, relative)

    return zip_name


#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_hash
# Description      : Calculates MD5 hash of file to detect modifications.
# Parameters       :
#   path -> File path
# Returns          :
#   MD5 hash string
#-----------------------------------------------------------------------------------------------------
def calculate_hash(path):

    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


#-----------------------------------------------------------------------------------------------------
# Function Name    : BackupFiles
# Description      : Copies only new or modified files from source to destination.
# Parameters       :
#   Source       -> Source directory
#   Destination  -> Backup directory
# Returns          :
#   List of copied files
#-----------------------------------------------------------------------------------------------------
def BackupFiles(Source, Destination):

    copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files


#-----------------------------------------------------------------------------------------------------
# Function Name    : DataShieldStart
# Description      : Executes backup process and appends results to history log.
# Parameters       :
#   Source      -> Source directory
#   LogFile     -> History log file name
#-----------------------------------------------------------------------------------------------------
def DataShieldStart(Source, LogFile):

    Border = "-" * 50
    BackupName = "BackupFiles"
    StartTime = time.ctime()

    print(Border)
    print("Backup process started")

    files = BackupFiles(Source, BackupName)
    zip_file = make_zip(BackupName)

    CreateLog(LogFile, files, StartTime, zip_file)

    print(Border)
    print("Backup completed successfully")
    print("Files copied :", len(files))
    print("Zip file created :", zip_file)
    print(Border)


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("--------- Data Shield System ----------")
    print(Border)

    if len(sys.argv) == 4 and sys.argv[1] == "--history":

        SourceDirectory = sys.argv[2]
        LogFileName = sys.argv[3]

        DataShieldStart(SourceDirectory, LogFileName)

    else:
        print("Usage:")
        print("ScriptName.py --history SourceDirectory LogFileName")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()