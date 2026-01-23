######################################################################################################
#  Lambda Function  : ReduceLambdaProduct
#  Input            : list
#  Output           : int
#  Description      : Returns the product of all numbers using lambda and reduce().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

from functools import reduce

# def ReduceLambdaProduct(No1,No2):
#     return No1 * No2

ReduceLambdaProduct = lambda No1, No2 : No1 * No2

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
    
    RData = reduce(ReduceLambdaProduct,Arr)

    # RData = reduce(lambda No1, No2 : No1 * No2 ,Arr)

    print("Product of all number is : ",RData)

if __name__ == "__main__":
    main()