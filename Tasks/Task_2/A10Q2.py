###########################################################################
#  Function name :     SumNatural
#  Input :             int 
#  Output :            int
#  Description :       It used to display summation of N natural number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def SumNatural(No):
    
    Result = 0

    if(No >= 0):
        for i in range(1,No+1):
            Result += i 
    else:
        print("Enter a Natural number greater than")
    
    return Result


def main():

    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = SumNatural(Value)
    print(Ret)

if __name__ == "__main__":
    main()