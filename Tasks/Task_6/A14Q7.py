######################################################################################################
#  Lambda Function  :     LambdaDivisible5
#  Input :                int 
#  Output :               bool
#  Description :          It is a lambda function used to return True if a number is Divisible by 5.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
######################################################################################################

# def LambdaDivisible5(No):
#     return (No % 5 == 0)


LambdaDivisible5 = lambda No : (No % 5 == 0)


def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = LambdaDivisible5(Value)
    print(Ret)
    

if __name__ == "__main__":
    main()