######################################################################################################
#  Program Name     : FilterMapReduceExample
#  Input            : list 
#  Output           : int
#  Description      : Filters numbers in range 70–90, increments them by 10,
#                     and returns the product using filter(), map(), and reduce().
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################

from functools import reduce

# def ChkRange(Brr):
#     flag = False
#     if((Brr >= 70) and (Brr <= 90)):
#         flag = True
    
#     return flag

ChkRange = lambda Brr : ((Brr >= 70 ) and (Brr <= 90))

# def Increment(Num):
#     return Num +10 

Increment = lambda Num : Num + 10

# def Product(No1 , No2):
#     Mult = No1 * No2

#     return Mult

Product = lambda No1, No2 : No1 * No2


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

    FData = list(filter(ChkRange,Arr))
    print(FData)

    MData = list(map(Increment,FData))
    print(MData)

    RData = reduce(Product,MData)
    print(RData)

if __name__ == "__main__":
    main()