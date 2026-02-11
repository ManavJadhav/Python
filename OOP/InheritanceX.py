class Parent :
    def __init__(self):
        print("Inside Parent cosntrcurtor")
        self.No1 = 10 
        self.No2 = 20

    def fun(self):
        print("Inside Fun method of Parent ",self.No1,self.No2)

class Child(Parent):
    def __init__(self):
        super().__init__()                  # compusolry if there is instance variable in Parent class
        print("Inside Child constructor")
        self.A = 11
        self.B = 21

    def sun(self):
        print("Inside Sun method of Child",self.A,self.B,self.No1,self.No2)

cobj = Child()

print(cobj.No1)     # 10
print(cobj.No2)     # 20

print(cobj.A)       # 11
print(cobj.B)       # 21

cobj.fun()
cobj.sun()

