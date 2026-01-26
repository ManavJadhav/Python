######################################################################################################
#  Lambda Function  : LambdaMultiplication
#  Input            : int , int
#  Output           : int
#  Description      : Returns the multiplication of two numbers using lambda.
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################

# def LambdaMultiplication(No1,No2):
#     return No1 * No2

LambdaMultiplication = lambda No1, No2 : No1 * No2

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())
    
    Ret = LambdaMultiplication(Value1,Value2)
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()