class Arithmetic : 
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object gets  created successfully")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithmetic(11,10)        # Arithmetic(id(obj1),11,10)        __init__(id(obj1),11,10)
obj2 = Arithmetic(21,20)        # Arithmetic(id(obj2),21,20)        __init__(id(obj2),21,20)

Ret = obj1.Addition()           # Addition(id(obj1))                Addition(1000)
print(Ret)                      # 21

Ret = obj2.Substraction()           # Substraction(id(obj2))                Substraction(2000)
print(Ret)                      # 1