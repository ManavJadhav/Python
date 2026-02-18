import hashlib
import os

def CalculateChecksum(Filename):
    fobj = open(Filename,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName= "Demo"):
    Ret = False

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName,SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)
            print(f"File name : {fname} Checksum :{Checksum}")

def main():
    DirectoryWatcher()

if __name__ =="__main__":
    main()