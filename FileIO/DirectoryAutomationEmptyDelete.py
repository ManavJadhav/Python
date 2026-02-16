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
    
    for FolderName,SubFolder,FileName in os.walk(DirName):

        for fname in FileName :
            fname = os.path.join(FolderName,fname)
            print("File name : ",fname)
            print("File size : ",os.path.getsize(fname))
            
            if(os.path.getsize(fname) == 0):            # Empty
                os.remove(fname)

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

if __name__ =="__main__":
    main()