###########################################################################
#  Function name :     Addition
#  Input :             int ,int 
#  Output :            int
#  Description :       It used to perform Addition of 2 numbers.
#
#  Function name :     Subtraction
#  Input :             int ,int 
#  Output :            int
#  Description :       It used to perform Subtraction of 2 numbers.

#  Function name :     Multiplication
#  Input :             int ,int 
#  Output :            int
#  Description :       It used to perform Multiplication of 2 numbers.

#  Function name :     Division
#  Input :             int ,int 
#  Output :            int
#  Description :       It used to perform Division of 2 numbers.
#
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def Addition(No1,No2):
    Sum = 0

    Sum = No1 + No2

    return Sum

def Subtraction(No1,No2):
    Sub = 0

    Sub = No1 - No2

    return Sub

def Multiplication(No1,No2):
    Mult = 0

    Mult = No1 * No2

    return Mult

def Division(No1,No2):
    Div = 0

    Div = No1 / No2

    return Div


def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    print("Addition is : ",Ret)

    Ret = Subtraction(Value1,Value2)
    print("Subtraction is : ",Ret)

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)

    Ret = Division(Value1,Value2)
    print("Division is : ",Ret)


if __name__ == "__main__":
    main()  