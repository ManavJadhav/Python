######################################################################################################
# Program Name     : PrimeNonPrimeThreaded
# Input            : List
# Output           : None
# Description      : Determines prime and non-prime numbers from a list using two separate threads
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################

import threading

def ChkPrime(No):
   
    if No < 2 :
       return False
   
    for i in range(2,No//2 +1 ):
       if (No % i == 0 ):
           return False
    
    return True

def DisplayPrime(Brr):
   print("Inside : ",threading.current_thread().name)

   for i in range(len(Brr)):
       if ChkPrime(Brr[i]) == True:
          print(f"{Brr[i]} is a prime number")
           

  

def DisplayNonPrime(Brr):
    print("Inside : ",threading.current_thread().name)

    for i in range(len(Brr)):
       if ChkPrime(Brr[i]) == False:
          print(f"{Brr[i]} is a NOT prime number")

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

    PrimeList = threading.Thread(target=DisplayPrime,args=(Arr,))
    NonPrimeList = threading.Thread(target=DisplayNonPrime,args=(Arr ,))

    PrimeList.start()
    NonPrimeList.start()

    PrimeList.join()
    NonPrimeList.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()