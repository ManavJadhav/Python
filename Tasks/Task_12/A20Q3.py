######################################################################################################
# Program Name     : SumEvenOddFromList
# Input            : List 
# Output           : int
# Description      : Calculates sum of even and odd numbers from a list using two threads
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################
import threading

#lobj = threading.Lock()

def SumEvenNumber(Brr):
   print("Inside : ",threading.current_thread().name)

   Sum = 0
   for i in range(len(Brr)):
       if((Brr[i] % 2 == 0)):
            # with lobj :
            Sum += Brr[i]
    
   print("Summation of all Even number from list is :",Sum)

  

def SumOddNumber(Brr):
    print("Inside : ",threading.current_thread().name)

    Sum = 0
    for i in range(len(Brr)):
       if((Brr[i] % 2 != 0)):
            # with lobj :
            Sum += Brr[i]
    
    print("Summation of all Odd number from list is :",Sum)

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

    EvenList = threading.Thread(target=SumEvenNumber,args=(Arr,))
    OddList = threading.Thread(target=SumOddNumber,args=(Arr ,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()