######################################################################################################
#  Lambda Function  : LambdaPower
#  Input            : int
#  Output           : int
#  Description      : Returns 2 raised to the power of the given number using lambda.
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################

# def LambdaPower(No):
#     return 2 ** No

LambdaPower = lambda No : 2 ** No

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())
    
    Ret = LambdaPower(Value)
    print("Power is : ",Ret)

if __name__ == "__main__":
    main()