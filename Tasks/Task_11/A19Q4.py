######################################################################################################
#  Program Name     : FilterMapReduceEvenSquareSum
#  Input            : list
#  Output           : int
#  Description      : Filters even numbers, squares them, and returns their sum
#                     using lambda, filter(), map(), and reduce().
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################

from functools import reduce

# def ChkEven(Brr):
#     flag = False
#     if((Brr % 2 )== 0):
#         flag = True
    
#     return flag

ChkEven = lambda Brr : (Brr % 2 ==0)

# def SquareX(Num):
#     return Num * Num 

SquareX = lambda Num : Num * Num

# def Add(No1 , No2):
#     Sum = No1 + No2

#     return Sum

Add = lambda No1, No2 : No1 + No2 


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

    FData = list(filter(ChkEven,Arr))
    print(FData)

    MData = list(map(SquareX,FData))
    print(MData)

    RData = reduce(Add,MData)
    print(RData)

if __name__ == "__main__":
    main()