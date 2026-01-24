###########################################################################
#  Function name :     ChkPrime
#  Input :             int 
#  Output :            bool
#  Description :       It used to check whether the number is Prime or not.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def main():
    Value = 0
    bRet = False

    print("Enter a number: ")
    Value = int(input())

    bRet = ChkPrime(Value)
    if(bRet == True):
        print("It is a Prime number")
    else:
        print("It is not a Prime number")


if __name__ == "__main__":
    main()