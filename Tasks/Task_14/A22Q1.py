######################################################################################################
# Program Name     : ClassInstanceDemo
# Input            : None
# Output           : Prints class variable and instance variable values
# Description      : Demonstrates object-oriented programming concepts including
#                   class variables, instance variables, instance methods,
#                   object creation, and object deletion.
# Author           : Manav Mahadev Jadhav
# Date             : 27/01/2026
######################################################################################################

class Demo:
    Value = 11

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def fun(self):
        print("Value of instance variable no1 & no2 from instance method fun is : ",self.no1, self.no2)

    def gun(self):
        print("Value of instance variable no1 & no2 from instance method gun is : ",self.no1, self.no2)

def main():
    
    obj1 = Demo(10,20)
    obj2 = Demo(51,101)

    print("Value of calss variable is : ",Demo.Value)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()

    del obj1
    del obj2

if __name__ == "__main__":
    main()