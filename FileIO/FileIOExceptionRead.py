def main():
    try :
        fobj = open("Hello.txt","r")            # fobj -> File handler ->  similar as fd
        print("File gets successfully opened")

        Data = fobj.read()

        print("Data from file is : ",Data)

        fobj.close() 

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")     

if __name__ =="__main__":
    main()