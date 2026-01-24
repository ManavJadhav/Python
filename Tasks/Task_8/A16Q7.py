###########################################################################
#  Function name :     ChkDivisibleBy5
#  Input :             int 
#  Output :            bool
#  Description :       It used to check whether the number is divisible by 5.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def ChkDivisibleBy5(No):
    flag = False
    if (No % 5 == 0):
        flag = True
    
    return flag


def main():
    Value = 0
    bRet = False

    print("Enter a number: ")
    Value = int(input())

    bRet = ChkDivisibleBy5(Value)
    print(bRet)

if __name__ == "__main__":
    main()