class Parent :
    def __init__(self):
        print("Inside Parent cosntrcurtor")

    def fun(self):
        print("Inside Fun method of Parent ")

class Child(Parent):
    def __init__(self):
        super().__init__()                  # compusolry if there is instance variable in Parent class
        print("Inside Child constructor")

    def fun(self):
        super().fun()
        print("Inside fun method of Child")

cobj = Child()

cobj.fun()
