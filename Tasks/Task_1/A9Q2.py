
###########################################################################
#  Function name :     ChkGreater
#  Input :             int , int
#  Output :            int
#  Description :       It used to find greater number from 2 number .
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkGreater(No1, No2):
    
    Result = 0
    
    if(No1 > No2):
        Result = No1
    else:
        Result = No2
    
    return Result


def main():

    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number: ")
    Value1 = int(input())

    print("Enter second number: ")
    Value2 = int(input())

    Ret = ChkGreater(Value1,Value2)
    print("The greater number is : ",Ret)

if __name__ == "__main__":
    main()