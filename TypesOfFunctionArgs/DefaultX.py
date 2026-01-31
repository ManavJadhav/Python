def EmpolyeeInfo(Name, Age, Salary ,City = "Mumbai"):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
   EmpolyeeInfo("Rahul",26,2000.50) 
   EmpolyeeInfo("Rahul",26,2000.50,"Pune")
   
if __name__ == "__main__":
    main()