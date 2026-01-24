###########################################################################
#  Module name :       Arithmetic
#  Input :             int, int 
#  Output :            int
#  Description :       It used to perform arithmetic operations on 2 numbers.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################
from Arithmetic import Addition
from Arithmetic import Subtraction
from Arithmetic import Multiplication
from Arithmetic import Division

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret =Addition(Value1,Value2)
    print("Addition is : ",Ret)

    Ret =Subtraction(Value1,Value2)
    print("Subtraction is : ",Ret)

    Ret =Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)

    Ret =Division(Value1,Value2)
    print("Division is : ",Ret)


if __name__ == "__main__":
    main()