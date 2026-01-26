######################################################################################################
# Program Name     : PrintNumbersThreaded
# Input            : None
# Output           : Numbers 1 to 50 and 50 to 1
# Description      : Prints numbers from 1 to 50 and then 50 to 1 using two threads
#                   and a threading.Lock to synchronize output.
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################

import threading

lobj = threading.Lock()

def Display():
   with lobj :
    print("Inside : ",threading.current_thread().name)
   
    for i in range(1,51):
        print(i)

  

def DisplayReverse():
    with lobj :
        print("Inside : ",threading.current_thread().name)

        for i in range(50,0,-1):
            print(i)

def main():
    
    print("Inside : ",threading.current_thread().name)

    Thread1 = threading.Thread(target=Display)
    Thread2 = threading.Thread(target=DisplayReverse)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()