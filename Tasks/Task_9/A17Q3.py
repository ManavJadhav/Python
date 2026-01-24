###########################################################################
#  Function name :     FactorialX
#  Input :             int 
#  Output :            int
#  Description :       It used to find factorial of a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def FactorialX(No):
    iFact = 1

    for i in range(1,No+1):
        iFact = iFact * i

    return iFact

def main():
    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = FactorialX(Value)
    print(f"Factorial of {Value} is :",Ret)


if __name__ == "__main__":
    main()