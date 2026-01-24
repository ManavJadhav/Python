###########################################################################
#  Function name :     CountDigits
#  Input :             int 
#  Output :            int
#  Description :       It used to return the count of digits in a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def CountDigits(No):
    iCnt = 0
    iDig = 0

    while(No != 0):
        iDig = No % 10
        iCnt += 1
        No = No // 10

    return iCnt    

def main():
    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = CountDigits(Value)
    print("Number of digits are : ", Ret)


if __name__ == "__main__":
    main()