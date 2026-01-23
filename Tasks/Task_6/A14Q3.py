##################################################################################################
#  Lambda Function  :     LambdaMaximum
#  Input :                int , int
#  Output :               int
#  Description :          It is a lambda function used to return maximum number from 2 numbers.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
##################################################################################################

# def LambdaMaximum(No1,No2):
#     return max(No1, No2) 

# def LambdaMaximum(No1,No2):
#     if(No1 > No2):
#       return No1 
#     else: 
#        return No2 

LambdaMaximum = lambda No1, No2 : max(No1,No2)

#LambdaMaximum = lambda No1, No2 : No1 if No1 >No2 else No2  

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = LambdaMaximum(Value1,Value2)
    print("Maximum number is : ",Ret)
    

if __name__ == "__main__":
    main()