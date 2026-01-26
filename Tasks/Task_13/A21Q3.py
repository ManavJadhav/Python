######################################################################################################
# Program Name     : ThreadSafeCounter
# Input            : None
# Output           : Final value of shared counter
# Description      : Demonstrates use of Lock to synchronize access to a shared
#                   global counter among multiple threads.
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################

import threading

iCnt = 0

lobj = threading.Lock()

def Update():
    global iCnt
    with lobj:
        print("Inside :", threading.current_thread().name)
        for i in range(100000):
            iCnt += 1

    print(iCnt)



def main():

    print("Inside : ",threading.current_thread().name)

    Thread1 = threading.Thread(target=Update)
    Thread2 = threading.Thread(target=Update)
    Thread3 = threading.Thread(target=Update)

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()