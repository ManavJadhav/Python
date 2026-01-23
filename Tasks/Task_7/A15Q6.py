######################################################################################################
#  Lambda Function  : ReduceLambdaMax
#  Input            : list
#  Output           : int
#  Description      : Returns the maximum number from the list using lambda and reduce().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

from functools import reduce

# def ReduceLambdaMin(No1,No2):
#     return min(No1 , No2)

ReduceLambdaMin = lambda No1, No2 : min(No1 , No2)

def main():
    Arr = list()
    Size = 0
    Value = 0

    print("Enter the number of Elements : ")
    Size = int(input())

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)
    
    RData = reduce(ReduceLambdaMin,Arr)

    # RData = reduce(lambda No1, No2 : min(No1 , No2),Arr)

    print("Minimum number from list is : ",RData)

if __name__ == "__main__":
    main()