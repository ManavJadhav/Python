######################################################################################################
#  Program Name     : FilterMapReducePrimeMax
#  Input            : list
#  Output           : int
#  Description      : Filters prime numbers from the list, multiplies each by 2,
#                     and returns the maximum value using filter(), map(), and reduce().
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################

from functools import reduce

def ChkPrime(Brr):
    if Brr < 2 :
        return False
    
    for i in range(2,Brr):
        if((Brr % i)==0):
            return False
    
    return True

# def MultBy2(Num):
#     return Num * 2 

MultBy2 = lambda Num : Num * 2

# def MaximumX(No1 , No2):
#     iMax = 0
#     if (No1 > No2):
#         iMax = No1
#     else:
#         iMax = No2

#     return iMax

MaximumX = lambda No1,No2 : max(No1,No2)


def main():
    Arr = list()
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    FData = list(filter(ChkPrime,Arr))
    print(FData)

    MData = list(map(MultBy2,FData))
    print(MData)

    RData = reduce(MaximumX,MData)
    print(RData)

if __name__ == "__main__":
    main()