######################################################################################################
# Program Name     : MaxMinThreaded
# Input            : List 
# Output           : None
# Description      : Finds maximum and minimum values from a list using two threads
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################

import threading

def DisplayMax(Brr):
   print("Inside : ",threading.current_thread().name)

   iMax = Brr[0]
   for i in range(len(Brr)):
       if(Brr[i] > iMax):
          iMax = Brr[i]
   
   print("Maximum number is : ",iMax)



def DisplayMin(Brr):
    print("Inside : ",threading.current_thread().name)

    iMin = Brr[0]

    for i in range(len(Brr)):
       if(Brr[i] < iMin):
          iMin = Brr[i]
   
    print("Minimum number is : ",iMin)

def main():
    
    Arr = list()
    Value = 0
    Size = 0

    print("Inside : ",threading.current_thread().name)

    print("Enter the number  of elements : ")
    Size  = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    Thread1 = threading.Thread(target=DisplayMax,args=(Arr,))
    Thread2 = threading.Thread(target=DisplayMin,args=(Arr ,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()