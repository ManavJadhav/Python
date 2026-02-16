import sys
import os
import time

def DirectoryScanner(DirName = "Demo"):
    
    Border = "-" * 50
    timestamp = time.ctime()

    Logfilename = "Demo%s.log" %(timestamp)
    Logfilename = Logfilename.replace(" ","_")
    Logfilename = Logfilename.replace(":","_")

    fobj = open(Logfilename,"w")
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Automation\n")
    fobj.write("This is a directory cleaner script\n")
    fobj.write(Border+"\n")

    Ret = False
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("there is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    for FolderName,SubFolder,FileName in os.walk(DirName):

        for fname in FileName :
            FileCount += 1 

            fname = os.path.join(FolderName,fname)
            
            if(os.path.getsize(fname) == 0):            # Empty
                EmptyFileCount += 1
                os.remove(fname)
    
    
    
    fobj.write("Total files scanned : "+str(FileCount)+"\n")
    fobj.write("Total empty file found : "+str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    Border = "-" * 40

    print(Border)
    print("-------- Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory ")
        return

    DirectoryScanner(sys.argv[1])


    print(Border)
    print("-------- Directory Automation ---------")
    print(Border)

if __name__ =="__main__":
    main()