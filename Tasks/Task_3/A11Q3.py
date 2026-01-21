
###########################################################################
#  Function name :     DigiSum
#  Input :             int 
#  Output :            int
#  Description :       It used to do summation of the digits in the number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def DigiSum(No):
    
    iDig = 0
    iCnt = 0
    Sum = 0

    if(No < 0):
        No = -No
    
    while(No != 0):
        iDig = int(No % 10)
        Sum += iDig
        iCnt = iCnt + 1
        No = int(No / 10)
    
    return Sum


def main():

    Value = 0 
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = DigiSum(Value)
    print(Ret)

if __name__ == "__main__":
    main()