######################################################################################################
#  Program Name     : SumOfEvenOddFactors
#  Input            : int
#  Output           : int
#  Description      : Calculates sum of even and odd factors using two threads.
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################

import threading

#lobj = threading.Lock()

def SumEvenFactor(No):
   # with lock :
   print("Inside : ",threading.current_thread().name)

   EvenSum = 0
   for i in range(1,No+1):
        if((No % i == 0 ))and(i % 2 == 0):
            print(i)
            EvenSum += i

   print("Summation of Even factor is : ",EvenSum)   

def SumOddFactors(No):
    # with lock :
    print("Inside : ",threading.current_thread().name)

    OddSum = 0
    for i in range(1,No+1):
        if((No % i == 0 ))and(i % 2 != 0):
            print(i)
            OddSum += i

    print("Summation of Odd factor is : ",OddSum)  

def main():
    
    Value = 0

    print("Enter a number : ")
    Value = int(input())

    EvenFactor = threading.Thread(target=SumEvenFactor,args=(Value,))
    OddFactor = threading.Thread(target=SumOddFactors,args=(Value ,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()