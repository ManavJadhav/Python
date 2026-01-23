#####################################################################################
#  Lambda Function  :     LambdaCube
#  Input :                int 
#  Output :               int
#  Description :          It is a lambda function used to return cube of a number.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
#####################################################################################

# def LambdaCube(No):
#     return No ** 3  

LambdaCube = lambda No : No ** 3
    

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = LambdaCube(Value)
    print(f"Cube of {Value} is : ",Ret)
    

if __name__ == "__main__":
    main()