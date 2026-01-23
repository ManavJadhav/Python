##################################################################################################
#  Lambda Function  :     LambdaAddition
#  Input :                int , int
#  Output :               int
#  Description :          It is a lambda function used to return Addition of 2 numbers.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
##################################################################################################

# def LambdaAddition(No1,No2):
#     return No1 + No2

LambdaAddition = lambda No1, No2 : No1 + No2


def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = LambdaAddition(Value1,Value2)
    print("Addition is : ",Ret)
    

if __name__ == "__main__":
    main()