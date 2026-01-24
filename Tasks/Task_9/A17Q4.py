###########################################################################
#  Function name :     FactorsSum
#  Input :             int 
#  Output :            int
#  Description :       It used to find summation of factors of a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def FactorsSum(No):
    Sum = 0 
    for i in range(1,No):
        if(No % i == 0):
            Sum += i
    return Sum

def main():
    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = FactorsSum(Value)
    print("Addition of factors is : ",Ret)


if __name__ == "__main__":
    main()