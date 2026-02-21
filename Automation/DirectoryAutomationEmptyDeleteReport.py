import sys
import os

def DirectoryScanner(DirName = "Demo"):
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
            print("File name : ",fname)
            print("File size : ",os.path.getsize(fname))
            
            if(os.path.getsize(fname) == 0):            # Empty
                EmptyFileCount += 1
                os.remove(fname)
    
    Border = "-" * 50
    print(Border)
    print("--------------- Automation  Report ---------------")
    print("Total files scanned : ",FileCount)
    print("Total empty file found : ",EmptyFileCount)
    print(Border)

def main():
    Border = "-" * 50

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