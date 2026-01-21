###########################################################################
#  Function name :     ChkPerfect
#  Input :             int 
#  Output :            bool
#  Description :       It used to check if a number is a perfect number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkPerfect(No):

    Sum = 0
    flag = False

    for i in range(1,No):
        if((No % i )==0):
            Sum = Sum + i 

    if(Sum == No):
        flag = True
    
    return flag
    

def main():
    Value = 0
    bRet = False

    print("Enter a number : ")
    Value = int(input())

    bRet = ChkPerfect(Value)
    if(bRet == True):
        print("It is a Perfect Number")
    else:
        print("It is NOT a Perfect Number")


if __name__ == "__main__":
    main()