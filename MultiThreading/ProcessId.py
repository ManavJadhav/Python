import os

def main():
    print("PID of  running process is : ",os.getpid())  # Main Process
    print("PID of Parent process is: ",os.getppid())    # CMD
    
if __name__ == "__main__":
    main()