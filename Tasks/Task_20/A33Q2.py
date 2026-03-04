#=====================================================================================================
# Program Name     : PlatformSurveillanceSystem
# Input            : TimeInterval (minutes) and DirectoryName (command line arguments)
# Output           : Periodic system monitoring log files generated inside specified directory
# Description      : Collects system information including CPU usage, RAM usage,
#                    disk usage, network statistics, and running process details.
#                    Automatically generates timestamped log files using scheduling.
# Author           : Manav Mahadev Jadhav
# Date             : 26/02/2026
#=====================================================================================================

import psutil
import sys
import os
import time
import schedule

#-----------------------------------------------------------------------------------------------------
# Function Name    : CreateLog
# Description      : Creates a timestamped log file in the specified directory
#                    and writes system monitoring information into it.
#-----------------------------------------------------------------------------------------------------
def CreateLog(FolderName):
    Border = "-" * 50

    # Check / Create directory
    if os.path.exists(FolderName):
        if not os.path.isdir(FolderName):
            print("Unable to create folder. A file with the same name exists.")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files created successfully.")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, f"SystemReport_{timestamp}.log")

    print("Log file created with name:", FileName)

    with open(FileName, "w") as fobj:

        fobj.write(Border + "\n")
        fobj.write("---- Platform Surveillance System ----\n")
        fobj.write("Log created at : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n")

        fobj.write("---------------- System Report -----------------\n")

        # CPU
        fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
        fobj.write(Border + "\n")

        # RAM
        mem = psutil.virtual_memory()
        fobj.write("RAM Usage : %s %%\n" % mem.percent)
        fobj.write(Border + "\n")

        # Disk
        fobj.write("\nDisk Usage Report\n")
        fobj.write(Border + "\n")

        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
            except:
                pass

        fobj.write(Border + "\n")

        # Network
        net = psutil.net_io_counters()
        fobj.write("\nNetwork Usage Report\n")
        fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
        fobj.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
        fobj.write(Border + "\n")

        # Process Details
        Data = ProcessScan()

        for info in Data:
            fobj.write("PID : %s\n" % info.get("pid"))
            fobj.write("Name : %s\n" % info.get("name"))
            fobj.write("UserName : %s\n" % info.get("username"))
            fobj.write("Status : %s\n" % info.get("status"))
            fobj.write("Start Time : %s\n" % info.get("create_time"))
            fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
            fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
            fobj.write("Threads Created : %d\n" % info.get("num_threads"))
            fobj.write("File Descriptors : %s\n" % info.get("num_fds"))
            fobj.write(Border + "\n")

        fobj.write(Border + "\n")
        fobj.write("--------------- End of Log File ---------------\n")
        fobj.write(Border + "\n")

#-----------------------------------------------------------------------------------------------------
# Function Name    : ProcessScan
# Description      : Scans all running processes and collects process-related
#                    information such as CPU usage, memory usage, thread count, etc.
#-----------------------------------------------------------------------------------------------------
def ProcessScan():
    listprocess = []

    # Warm up CPU percent calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])

            try:
                info["create_time"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.localtime(info["create_time"])
                )
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["num_threads"] = proc.num_threads()

            try:
                info["num_fds"] = proc.num_fds()
            except:
                info["num_fds"] = "Access Denied"

            listprocess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program. Parses command line arguments
#                    and schedules automatic log generation.
#-----------------------------------------------------------------------------------------------------
def main():
    Border = "-" * 50
    print(Border)
    print("---- Platform Surveillance System ----")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("This script performs periodic system monitoring.")
            print("It collects CPU, RAM, disk, network, and process information.")
            print("Log files are generated automatically.")

        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage:")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes for periodic scheduling")
            print("DirectoryName: Directory to store log files")

        else:
            print("Invalid option. Use --h or --u for help.")

    elif len(sys.argv) == 3:

        print("Time Interval (minutes):", sys.argv[1])
        print("Directory Name:", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started successfully.")
        print("Press Ctrl + C to stop execution.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments.")
        print("Use --h or --u for usage details.")

    print(Border)
    print("--------- Thank you for using the script ---------")
    print(Border)


if __name__ == "__main__":
    main()