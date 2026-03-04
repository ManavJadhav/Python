#=====================================================================================================
# Program Name     : DataShieldSystem
# Input            : SourceDirectory LogDirectory
# Output           : Backup of new/modified files (excluding ignored types) with zip archive
# Description      :
#   - Copies only new or modified files
#   - Ignores specific file extensions (.tmp, .log, .exe)
#   - Creates compressed archive of backup
#   - Generates detailed log file
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
# Description      : Generates backup log file containing copied files and zip archive name.
# Parameters       :
#   FolderName  -> Directory to store log file
#   files       -> List of copied files
#   StartTime   -> Backup start time
#   zip_file    -> Generated zip file name
# Returns          :
#   Log file path
#-----------------------------------------------------------------------------------------------------
def CreateLog(FolderName, files, StartTime, zip_file):

    Border = "-" * 50
    os.makedirs(FolderName, exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, f"BackupLog_{timestamp}.log")

    print("Log file created:", FileName)

    with open(FileName, "w") as fobj:

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

    return FileName


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
# Description      : Copies only new or modified files while ignoring
#                    specific extensions.
# Parameters       :
#   Source       -> Source directory
#   Destination  -> Backup directory
# Returns          :
#   List of copied files (relative paths)
#-----------------------------------------------------------------------------------------------------
def BackupFiles(Source, Destination):

    copied_files = []
    ignore_extensions = (".tmp", ".log", ".exe")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            if file.lower().endswith(ignore_extensions):
                continue

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
# Description      : Executes backup process and log creation.
# Parameters       :
#   Source      -> Source directory
#   FolderName  -> Log directory
#-----------------------------------------------------------------------------------------------------
def DataShieldStart(Source, FolderName):

    Border = "-" * 50
    BackupName = "BackupFiles"
    StartTime = time.ctime()

    print(Border)
    print("Backup process started")

    files = BackupFiles(Source, BackupName)
    zip_file = make_zip(BackupName)

    CreateLog(FolderName, files, StartTime, zip_file)

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

    if len(sys.argv) == 3:

        SourceDirectory = sys.argv[1]
        LogDirectory = sys.argv[2]

        DataShieldStart(SourceDirectory, LogDirectory)

    else:
        print("Usage:")
        print("ScriptName.py SourceDirectory LogDirectory")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()