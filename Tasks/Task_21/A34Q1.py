#=====================================================================================================
# Program Name     : DataShieldSystem
# Input            : TimeInterval (seconds), SourceDirectory, LogDirectory
# Output           : Periodic backup of new/modified files with zip archive and log generation
# Description      : 
#   - Copies only new or modified files from source to backup directory
#   - Creates a compressed zip archive of the backup
#   - Generates a detailed log file
#   - Executes periodically using scheduling
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
# Function Name    : CreateLog
# Description      : Creates a timestamped log file containing backup details,
#                    list of copied files, and generated zip archive name.
# Parameters       :
#   FolderName  -> Directory where log file will be stored
#   files       -> List of copied files
#   StartTime   -> Backup start time
#   zip_file    -> Generated zip file name
#-----------------------------------------------------------------------------------------------------
def CreateLog(FolderName, files, StartTime, zip_file):

    Border = "-" * 50

    if os.path.exists(FolderName):
        if not os.path.isdir(FolderName):
            print("Error: A file with the same name as log directory exists.")
            return
    else:
        os.makedirs(FolderName, exist_ok=True)
        print("Log directory created successfully.")

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
            fobj.write("File Name : " + file + "\n")

        fobj.write("\n" + Border + "\n")
        fobj.write("Zip File Generated:\n")
        fobj.write(Border + "\n")
        fobj.write("Zip Name : " + zip_file + "\n")
        fobj.write(Border + "\n")


#-----------------------------------------------------------------------------------------------------
# Function Name    : make_zip
# Description      : Creates a zip archive of the given folder.
# Parameters       :
#   folder -> Folder to be compressed
# Returns          :
#   Name of generated zip file
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
# Description      : Calculates MD5 hash of a file for change detection.
# Parameters       :
#   path -> File path
# Returns          :
#   MD5 hash string
#-----------------------------------------------------------------------------------------------------
def calculate_hash(path):

    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


#-----------------------------------------------------------------------------------------------------
# Function Name    : BackupFiles
# Description      : Copies only new or modified files from source directory
#                    to destination directory.
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
# Description      : Executes backup process, creates zip archive,
#                    and generates log file.
# Parameters       :
#   Source      -> Source directory to backup
#   FolderName  -> Directory to store log files
#-----------------------------------------------------------------------------------------------------
def DataShieldStart(Source="Data", FolderName="LogData"):

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
# Description      : Entry point of program. Handles command line arguments
#                    and schedules periodic backup execution.
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("--------- Data Shield System ----------")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("1 : Takes automatic backup at given interval")
            print("2 : Backs up only new or updated files")
            print("3 : Creates compressed archive of backup periodically")

        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage:")
            print("ScriptName.py TimeInterval SourceDirectory LogFolderName")
            print("TimeInterval : Time in seconds for periodic scheduling")
            print("SourceDirectory: Directory to be backed up")
            print("LogFolderName : Directory to store logs")

        else:
            print("Invalid option. Use --h or --u.")

    elif len(sys.argv) == 4:

        TimeInterval = int(sys.argv[1])
        SourceDirectory = sys.argv[2]
        LogDirectory = sys.argv[3]

        schedule.every(TimeInterval).seconds.do(
            DataShieldStart,
            SourceDirectory,
            LogDirectory
        )

        print(Border)
        print("Data Shield System started successfully")
        print("Time interval (seconds):", TimeInterval)
        print("Press Ctrl + C to stop")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments. Use --h or --u.")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()