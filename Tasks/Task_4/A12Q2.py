###########################################################################
#  Function name :     FactorX
#  Input :             int 
#  Output :            list
#  Description :       It used to find factors of a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def FactorX(No):
    Result = []

    for i in range(1,No+1):
        if((No % i)==0 ):
            Result.append(i)
    
    return Result


def main():
    
    Value = 0
    Ret = 0

    print("Enter a number : ")
    Value = int(input())

    Ret = FactorX(Value)
    print(Ret)


if __name__ == "__main__":
    main()