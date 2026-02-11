class Parent :
    def __init__(self):
        print("Inside Parent cosntrcurtor")
        self.No1 = 10 
        self.No2 = 20

    def fun(self):
        print("Inside Fun method of Parent ")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
        self.A = 11
        self.B = 21

    def sun(self):
        print("Inside Sun method of Child")

cobj = Child()