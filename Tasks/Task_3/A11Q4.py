
###########################################################################
#  Function name :     ReverseX
#  Input :             int 
#  Output :            int
#  Description :       It used to reverse the number.
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


def main():

    Value = 0 
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = ReverseX(Value)
    print(Ret)

if __name__ == "__main__":
    main()