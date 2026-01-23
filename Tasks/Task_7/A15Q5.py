######################################################################################################
#  Lambda Function  : ReduceLambdaMax
#  Input            : list
#  Output           : int
#  Description      : Returns the maximum number from the list using lambda and reduce().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

from functools import reduce

# def ReduceLambdaMax(No1,No2):
#     return max(No1 , No2)

ReduceLambdaMax = lambda No1, No2 : max(No1 , No2)

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
    
    RData = reduce(ReduceLambdaMax,Arr)

    # RData = reduce(lambda No1, No2 : max(No1 , No2),Arr)

    print("Maximum number from list is : ",RData)

if __name__ == "__main__":
    main()