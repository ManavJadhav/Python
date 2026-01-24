###########################################################################
#  Function name :     Add
#  Input :             int , int 
#  Output :            int
#  Description :       It used to do summation of 2 numbers.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def Add(No1,No2):
    Sum = 0 
    Sum = No1 + No2
    return Sum


def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the first number: ")
    Value1 = int(input())

    print("Enter the second number: ")
    Value2 = int(input())

    Ret = Add(Value1,Value2)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()