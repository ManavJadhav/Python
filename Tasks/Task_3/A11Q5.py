
###########################################################################
#  Function name :     PallindromeX
#  Input :             int 
#  Output :            bool
#  Description :       It used to check if the number is a Pallindrome.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ReverseX(No):
    
    iDig = 0
    iCnt = 0
    Rev = 0

    if(No < 0):
        No = -No
    
    while(No != 0):
        iDig = int(No % 10)
        Rev = (Rev * 10) + iDig 
        No = int(No / 10)
    
    return Rev


def PallindromeX(Num):
    
    flag = False
    Result = ReverseX(Num)

    if(Result == Num ):
        flag = True
    
    return flag


def main():

    Value = 0 
    bRet = 0

    print("Enter a number: ")
    Value = int(input())

    bRet = PallindromeX(Value)
    if(bRet == True):
        print("It is a Pallindrome ")
    else:
        print("It is NOT a Pallindrome ")

if __name__ == "__main__":
    main()