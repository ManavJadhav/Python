#=====================================================================================================
# Program Name     : PlatformSurveillanceSystem
# Input            : TimeInterval (minutes) and DirectoryName (command line arguments)
# Output           : Periodic system monitoring log files generated inside specified directory
# Description      : Collects detailed system information including CPU usage, RAM usage,
#                    disk usage, network statistics, and running process details.
#                    Generates timestamped log files automatically using scheduling.
#                    Includes memory analysis and top memory-consuming processes.
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
# Description      : Creates a timestamped log file and writes complete system
#                    monitoring information including process memory analysis.
#-----------------------------------------------------------------------------------------------------
def CreateLog(FolderName):

    Border = "-" * 50

    # Create directory safely
    if os.path.exists(FolderName):
        if not os.path.isdir(FolderName):
            print("Unable to create folder. A file with same name exists.")
            return
    else:
        os.makedirs(FolderName, exist_ok=True)
        print("Directory for log files created successfully.")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, f"SystemReport_{timestamp}.log")

    print("Log file created with name:", FileName)

    with open(FileName, "w") as fobj:

        fobj.write(Border + "\n")
        fobj.write("---- Platform Surveillance System ----\n")
        fobj.write("Log created at : " + time.ctime() + "\n")
        fobj.write(Border + "\n\n")

        # ---------------- SYSTEM REPORT ----------------
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

        # ---------------- PROCESS REPORT ----------------
        Data = ProcessScan()

        fobj.write("\n---------------- Process Details ----------------\n")

        for info in Data:

            mem_info = info.get("memory_info")

            fobj.write("PID : %s\n" % info.get("pid"))
            fobj.write("Name : %s\n" % info.get("name"))
            fobj.write("UserName : %s\n" % info.get("username"))
            fobj.write("Status : %s\n" % info.get("status"))
            fobj.write("Start Time : %s\n" % info.get("create_time"))
            fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
            fobj.write("Threads Created : %d\n" % info.get("num_threads"))
            fobj.write("File Descriptors : %s\n" % info.get("num_fds"))

            # Memory Breakdown
            fobj.write("RAM Used (RSS) : %.2f MB\n" % (mem_info.rss / (1024 * 1024)))
            fobj.write("Virtual Memory (VMS) : %.2f MB\n" % (mem_info.vms / (1024 * 1024)))
            fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
            fobj.write(Border + "\n")

        # ---------------- TOP 10 MEMORY CONSUMERS ----------------
        Top10 = sorted(
            Data,
            key=lambda x: x["memory_info"].rss,
            reverse=True
        )[:10]

        fobj.write("\n---------- Top 10 Memory Consuming Processes ----------\n")

        for info in Top10:

            mem_info = info.get("memory_info")

            fobj.write("PID : %s\n" % info.get("pid"))
            fobj.write("Name : %s\n" % info.get("name"))
            fobj.write("RAM Used (RSS) : %.2f MB\n" % (mem_info.rss / (1024 * 1024)))
            fobj.write("Virtual Memory (VMS) : %.2f MB\n" % (mem_info.vms / (1024 * 1024)))
            fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
            fobj.write(Border + "\n")

        fobj.write(Border + "\n")
        fobj.write("--------------- End of Log File ---------------\n")
        fobj.write(Border + "\n")


#-----------------------------------------------------------------------------------------------------
# Function Name    : ProcessScan
# Description      : Scans all running processes and collects detailed
#                    process information including memory usage.
#-----------------------------------------------------------------------------------------------------
def ProcessScan():

    listprocess = []

    # Warm up CPU calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(
                attrs=["pid", "name", "username", "status", "create_time"]
            )

            # Format time
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

            info["memory_info"] = proc.memory_info()

            listprocess.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point. Parses command line arguments and schedules
#                    periodic system monitoring.
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("---- Platform Surveillance System ----")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("This script performs automated system monitoring.")
            print("It logs CPU, RAM, disk, network and process details.")
            print("Includes detailed memory analysis and top memory ranking.")

        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage:")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes for scheduling")
            print("DirectoryName: Directory to store log files")

        else:
            print("Invalid option. Use --h or --u for help.")

    elif len(sys.argv) == 3:

        print("Time Interval :", sys.argv[1])
        print("Directory Name :", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started successfully.")
        print("Press Ctrl + C to stop execution.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments.")
        print("Use --h or --u for help.")

    print(Border)
    print("--------- Thank you for using this script ---------")
    print(Border)


if __name__ == "__main__":
    main()