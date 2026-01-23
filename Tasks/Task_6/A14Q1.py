#####################################################################################
#  Lambda Function  :     LambdaSqaure
#  Input :                int 
#  Output :               int
#  Description :          It is a lambda function used to return square of a number.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
#####################################################################################

# def LambdaSqaure(No):
#     return No ** 2   

LambdaSqaure = lambda No : No ** 2
    

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = LambdaSqaure(Value)
    print(f"Square of {Value} is :",Ret)
    

if __name__ == "__main__":
    main()