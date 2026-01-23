##################################################################################################
#  Lambda Function  :     LambdaMaximum
#  Input :                int , int
#  Output :               int
#  Description :          It is a lambda function used to return maximum number from 3 numbers.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
##################################################################################################

# def LambdaMaximum(No1,No2,No3):
#     return max(No1,No2,No3) 

LambdaMaximum = lambda No1, No2 , No3 : max(No1,No2,No3)


def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    print("Enter the third number : ")
    Value3 = int(input())

    Ret = LambdaMaximum(Value1,Value2,Value3)
    print("Maximum number is : ",Ret)
    

if __name__ == "__main__":
    main()