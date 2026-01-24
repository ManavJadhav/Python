###########################################################################
#  Function name :     ChkNum
#  Input :             int 
#  Output :            bool
#  Description :       It used to check whether the number is Even or Odd.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def ChkNum(No):
    flag = False
    if (No % 2 == 0):
        flag = True
    
    return flag


def main():
    Value = 0
    bRet = False

    print("Enter a number: ")
    Value = int(input())

    bRet = ChkNum(Value)
    if(bRet == True):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()