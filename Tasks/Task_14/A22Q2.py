######################################################################################################
# Program Name     : CircleAreaCircumference
# Input            : Radius of circle (float)
# Output           : Prints area and circumference of the circle
# Description      : Demonstrates object-oriented programming by calculating
#                   area and circumference of a circle using class methods,
#                   class variables, and multiple objects.
# Author           : Manav Mahadev Jadhav
# Date             : 27/01/2026
######################################################################################################

class Cicrle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area =  0.0
        self.Circumference = 0.0

    def Accept(self,A):
        self.Radius = A

    def CalculateArea(self):
        print(self.Radius)
        self.Area = Cicrle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Cicrle.PI * self.Radius
    
    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference)
    
def main():

    No = 0.0
    print("Enter the radius of circle : ")
    No = float(input())

    obj1 = Cicrle()
    obj2 = Cicrle()

    obj1.Accept(No)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    print("-"*50)

    No = 0.0
    print("Enter the radius of circle : ")
    No = float(input())

    obj2.Accept(No)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()


if __name__ == "__main__":
    main()