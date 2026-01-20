
###########################################################################
#  Function name :     ChkDivisible
#  Input :             int 
#  Output :            int
#  Description :       It used to check if a number is divisible by 3 and 5.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkDivisible(No):
    
    flag  = False
    if((No % 3)==0 and (No % 5)==0):
        flag = True
    return flag


def main():

    Value = 0 
    bRet = False

    print("Enter a number: ")
    Value = int(input())

    bRet = ChkDivisible(Value)
    if(bRet == True ):
        print("It is divisible by 3 and 5")
    else:
        print("It is NOT divisible by 3 and 5")
    

if __name__ == "__main__":
    main()