#############################################################################################
#  Lambda Function  :     LambdaEven
#  Input :                int 
#  Output :               bool
#  Description :          It is a lambda function used to return True if a number is Even.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
#############################################################################################

# def LambdaEven(No1):
#     return (No % 2 == 0)


LambdaEven = lambda No : (No % 2 == 0)


def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = LambdaEven(Value)
    print(Ret)
    

if __name__ == "__main__":
    main()