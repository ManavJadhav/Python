##################################################################################################
#  Lambda Function  :     LambdaMinimum
#  Input :                int , int
#  Output :               int
#  Description :          It is a lambda function used to return minimum number from 2 numbers.
#  Author :               Manav Mahadev Jadhav
#  Date :                 22/01/2026
#
##################################################################################################

# def LambdaMinimum(No1,No2):
#     return min(No1, No2) 

# def LambdaMinimum(No1,No2):
#     if(No1 > No2):
#       return No2
#     else: 
#        return No1 

LambdaMinimum = lambda No1, No2 : min(No1,No2)

#LambdaMinimum = lambda No1, No2 : No2 if No1 >No2 else No1  

def main():
    Value1 = 0
    Value2 = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Ret = LambdaMinimum(Value1,Value2)
    print("Minimum number is : ",Ret)
    

if __name__ == "__main__":
    main()