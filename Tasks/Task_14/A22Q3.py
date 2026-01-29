######################################################################################################
# Program Name     : ArithmeticOperations
# Input            : Two integers
# Output           : Prints addition, subtraction, multiplication, and division
# Description      : Demonstrates object-oriented programming by performing
#                   basic arithmetic operations using class methods.
# Author           : Manav Mahadev Jadhav
# Date             : 27/01/2026
######################################################################################################
class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 =  0

    def Accept(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def Addition(self):
        Sum = 0
        Sum = self.Value1 + self.Value2

        return Sum

    def Substraction(self):
        Sub = 0
        Sub = self.Value1 - self.Value2

        return Sub
    
    def Multiplication(self):
        Mult = 0
        Mult = self.Value1 * self.Value2

        return Mult

    def Division(self):
        Div = 0
        Div = self.Value1 / self.Value2

        return Div
    
    
def main():

    No1 = 0
    No2 = 0
    Ret = 0

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    obj1 = Arithmetic()
    obj1.Accept(No1,No2)

    obj2 = Arithmetic()
    obj2.Accept(No1,No2)

    Ret = obj1.Addition()
    print("Addition is : ",Ret)

    Ret = obj1.Substraction()
    print("Substraction is : ",Ret)

    Ret = obj2.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj2.Division()
    print("Division is : ",Ret)


if __name__ == "__main__":
    main()