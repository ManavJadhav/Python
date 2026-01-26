######################################################################################################
# Program Name     : SumProductThreaded
# Input            : List 
# Output           : Prints sum and product of list elements
# Description      : Calculates the sum and product of elements from a list
#                   using two separate threads.
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################
import threading

def SumOfElements(Brr):

    print("Inside : ",threading.current_thread().name)

    iSum  = 0
    for i in range(len(Brr)):
       iSum = iSum + Brr[i]
   
    print("Summation of elements is : ",iSum)



def ProductOfElements(Brr):
    print("Inside : ",threading.current_thread().name)

    iMult  = 1
    for i in range(len(Brr)):
       iMult = iMult * Brr[i]
   
    print("Product of elements is : ",iMult)

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

    Thread1 = threading.Thread(target=SumOfElements,args=(Arr,))
    Thread2 = threading.Thread(target=ProductOfElements,args=(Arr ,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from : ",threading.current_thread().name)

if __name__ == "__main__":
    main()