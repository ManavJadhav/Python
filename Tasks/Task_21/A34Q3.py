#=====================================================================================================
# Program Name     : DataShieldSystem
# Input            : 
#   Backup Mode   -> TimeInterval SourceDirectory LogDirectory
#   Restore Mode  -> --restore ZipFile DestinationDirectory
# Output           : Backup with zip + optional restore capability
# Description      :
#   - Copies only new/modified files
#   - Creates zip archive
#   - Generates log file
#   - Supports restore from zip archive
# Author           : Manav Mahadev Jadhav
# Date             : 26/02/2026
#=====================================================================================================

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile


#-----------------------------------------------------------------------------------------------------
# Function Name    : extract_zip
# Description      : Extracts given zip file into destination directory.
# Parameters       :
#   Dest      -> Destination directory
#   zip_file  -> Zip file to extract
#-----------------------------------------------------------------------------------------------------
def extract_zip(Dest, zip_file):

    if not os.path.exists(zip_file):
        print("Error: Zip file does not exist.")
        return

    os.makedirs(Dest, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_file, 'r') as ext:
            ext.extractall(Dest)
        print("Restore completed successfully.")
    except Exception as e:
        print("Restore failed:", e)


#-----------------------------------------------------------------------------------------------------
# Function Name    : CreateLog
# Description      : Generates backup log file.
# Parameters       :
#   FolderName  -> Log directory
#   files       -> Copied files list
#   StartTime   -> Backup start time
#   zip_file    -> Created zip file
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
# Description      : Copies new or modified files from source to destination.
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
# Description      : Entry point. Supports backup scheduling and restore mode.
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("--------- Data Shield System ----------")
    print(Border)

    # Restore Mode
    if len(sys.argv) == 4 and sys.argv[1] == "--restore":

        zip_file = sys.argv[2]
        destination = sys.argv[3]

        extract_zip(destination, zip_file)

    # Backup Mode (Scheduled)
    elif len(sys.argv) == 4:

        TimeInterval = int(sys.argv[1])
        SourceDirectory = sys.argv[2]
        LogDirectory = sys.argv[3]

        schedule.every(TimeInterval).seconds.do(
            DataShieldStart,
            SourceDirectory,
            LogDirectory
        )

        print("Backup system started.")
        print("Time interval (seconds):", TimeInterval)
        print("Press Ctrl + C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("Backup  : ScriptName.py TimeInterval SourceDirectory LogDirectory")
        print("Restore : ScriptName.py --restore ZipFile DestinationDirectory")

    print(Border)


if __name__ == "__main__":
    main()