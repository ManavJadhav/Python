
###########################################################################
#  Function name :     ChkPrime
#  Input :             Integer 
#  Output :            bool
#  Description :       It used to check whether the number is a Prime Number or Not.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkPrime(No):
    
    flag  = False
    
    for i in range(2, No):
        if((No % i)==0):
            flag = False
            break
        else:
            flag = True

    return flag


def main():

    Value = 0 
    bRet = False

    print("Enter a number: ")
    Value = int(input())

    bRet = ChkPrime(Value)
    if(bRet == True ):
        print("It is a Prime Number")
    else:
        print("It is NOT a Prime Number")
    

if __name__ == "__main__":
    main()