#=====================================================================================================
# Program Name     : PlatformSurveillanceSystem
# Input            : DirectoryName, ReceiverEmail, TimeInterval (minutes)
# Output           : Periodic system monitoring log files emailed to receiver
# Description      : Collects detailed system information including CPU usage,
#                    RAM usage, disk usage, network statistics and running process details.
#                    Generates timestamped log files and sends them via email
#                    automatically using scheduling.
# Author           : Manav Mahadev Jadhav
# Date             : 26/02/2026
#=====================================================================================================

import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage


#-----------------------------------------------------------------------------------------------------
# Function Name    : SendMail
# Description      : Creates log file and sends it as an email attachment
#-----------------------------------------------------------------------------------------------------
def SendMail(FolderName, ReceiverEmail):

    FileName = CreateLog(FolderName)

    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not sender_email or not app_password:
        print("Error: Email credentials not set as environment variables.")
        return

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = ReceiverEmail
    msg["Subject"] = "Platform Surveillance System Report"

    msg.set_content("Automated system monitoring log attached.\n\nRegards,\nManav Jadhav")

    with open(FileName, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(FileName)
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Email sent successfully to", ReceiverEmail)


#-----------------------------------------------------------------------------------------------------
# Function Name    : CreateLog
# Description      : Generates timestamped system monitoring log file
#-----------------------------------------------------------------------------------------------------
def CreateLog(FolderName):

    Border = "-" * 50

    os.makedirs(FolderName, exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, f"SystemReport_{timestamp}.log")

    print("Log file created:", FileName)

    with open(FileName, "w") as fobj:

        fobj.write(Border + "\n")
        fobj.write("---- Platform Surveillance System ----\n")
        fobj.write("Log created at : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n")

        fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
        fobj.write(Border + "\n")

        mem = psutil.virtual_memory()
        fobj.write("RAM Usage : %s %%\n" % mem.percent)
        fobj.write(Border + "\n")

        fobj.write("\nDisk Usage Report\n")
        fobj.write(Border + "\n")

        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
            except:
                pass

        fobj.write(Border + "\n")

        net = psutil.net_io_counters()
        fobj.write("\nNetwork Usage Report\n")
        fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
        fobj.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
        fobj.write(Border + "\n")

        Data = ProcessScan()

        for info in Data:

            mem_info = info["memory_info"]

            fobj.write("PID : %s\n" % info["pid"])
            fobj.write("Name : %s\n" % info["name"])
            fobj.write("CPU %% : %.2f\n" % info["cpu_percent"])
            fobj.write("Threads : %d\n" % info["num_threads"])
            fobj.write("RAM Used (RSS) : %.2f MB\n" % (mem_info.rss / (1024 * 1024)))
            fobj.write("Memory %% : %.2f\n" % info["memory_percent"])
            fobj.write(Border + "\n")

        Top10 = sorted(Data, key=lambda x: x["memory_info"].rss, reverse=True)[:10]

        fobj.write("\nTop 10 Memory Consuming Processes\n")
        fobj.write(Border + "\n")

        for info in Top10:
            mem_info = info["memory_info"]
            fobj.write("PID : %s | Name : %s | RSS : %.2f MB\n" %
                       (info["pid"], info["name"], mem_info.rss / (1024 * 1024)))

        fobj.write("\n" + Border + "\n")

    return FileName


#-----------------------------------------------------------------------------------------------------
# Function Name    : ProcessScan
# Description      : Collects detailed information of running processes
#-----------------------------------------------------------------------------------------------------
def ProcessScan():

    processes = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name"])

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["num_threads"] = proc.num_threads()
            info["memory_info"] = proc.memory_info()

            processes.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("---- Platform Surveillance System ----")
    print(Border)

    if len(sys.argv) == 4:

        DirectoryName = sys.argv[1]
        ReceiverEmail = sys.argv[2]
        TimeInterval = int(sys.argv[3])

        schedule.every(TimeInterval).minutes.do(
            SendMail,
            DirectoryName,
            ReceiverEmail
        )

        print("System monitoring started.")
        print("Press Ctrl + C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("python ScriptName.py DirectoryName ReceiverEmail TimeInterval")

    print(Border)


if __name__ == "__main__":
    main()