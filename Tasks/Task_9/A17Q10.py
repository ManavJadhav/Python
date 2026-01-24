###########################################################################
#  Function name :     SumDigits
#  Input :             int 
#  Output :            int
#  Description :       It used to return the summation of digits in a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def SumDigits(No):
    Sum = 0
    iDig = 0

    while(No != 0):
        iDig = No % 10
        Sum += iDig
        No = No // 10

    return Sum    

def main():
    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = SumDigits(Value)
    print("Summation of digit is : ", Ret)


if __name__ == "__main__":
    main()