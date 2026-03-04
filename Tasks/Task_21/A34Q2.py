#=====================================================================================================
# Program Name     : DataShieldSystem
# Input            : TimeInterval (seconds), SourceDirectory, LogDirectory, ReceiverEmail
# Output           : Periodic backup of new/modified files with zip archive and email delivery
# Description      :
#   - Copies only new or modified files
#   - Creates compressed archive of backup
#   - Generates detailed log file
#   - Emails log and zip file as attachment
#   - Executes periodically using scheduler
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
import smtplib
from email.message import EmailMessage


#-----------------------------------------------------------------------------------------------------
# Function Name    : SendMail
# Description      : Sends given files as email attachments using SMTP SSL.
# Parameters       :
#   Files           -> List of file paths to attach
#   receiver_email  -> Recipient email address
#-----------------------------------------------------------------------------------------------------
def SendMail(Files, receiver_email):

    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not sender_email or not app_password:
        print("Error: Email credentials not set in environment variables.")
        return

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Data Shield System Backup Report"

    msg.set_content(
        "Automated backup completed successfully.\n\nRegards,\nManav Jadhav"
    )

    # Attach files safely
    for FileName in Files:
        if os.path.exists(FileName):
            with open(FileName, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=os.path.basename(FileName)
                )

    # Secure SMTP connection
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        print("Email sent successfully to", receiver_email)
    except Exception as e:
        print("Failed to send email:", e)


#-----------------------------------------------------------------------------------------------------
# Function Name    : CreateLog
# Description      : Generates backup log file containing copied files and zip archive name.
# Parameters       :
#   FolderName  -> Directory to store log file
#   files       -> List of copied files
#   StartTime   -> Backup start time
#   zip_file    -> Generated zip file name
# Returns          :
#   Generated log file path
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
# Description      : Calculates MD5 hash of a file to detect modifications.
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
#   List of copied file relative paths
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
# Description      : Executes backup, zip creation, log generation and email sending.
# Parameters       :
#   Source          -> Source directory
#   FolderName      -> Log directory
#   receiver_email  -> Email recipient
#-----------------------------------------------------------------------------------------------------
def DataShieldStart(Source, FolderName, receiver_email):

    Border = "-" * 50
    BackupName = "BackupFiles"
    StartTime = time.ctime()

    print(Border)
    print("Backup process started")

    files = BackupFiles(Source, BackupName)
    zip_file = make_zip(BackupName)
    log_file = CreateLog(FolderName, files, StartTime, zip_file)

    SendMail([log_file, zip_file], receiver_email)

    print(Border)
    print("Backup completed successfully")
    print("Files copied :", len(files))
    print("Zip file created :", zip_file)
    print(Border)


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point. Parses arguments and schedules periodic execution.
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("--------- Data Shield System ----------")
    print(Border)

    if len(sys.argv) == 5:

        TimeInterval = int(sys.argv[1])
        SourceDirectory = sys.argv[2]
        LogDirectory = sys.argv[3]
        ReceiverEmail = sys.argv[4]

        schedule.every(TimeInterval).seconds.do(
            DataShieldStart,
            SourceDirectory,
            LogDirectory,
            ReceiverEmail
        )

        print("System started successfully.")
        print("Time interval (seconds):", TimeInterval)
        print("Press Ctrl + C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("ScriptName.py TimeInterval SourceDirectory LogFolderName ReceiverEmail")

    print(Border)


if __name__ == "__main__":
    main()