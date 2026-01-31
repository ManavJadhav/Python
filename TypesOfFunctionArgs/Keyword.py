def EmpolyeeInfo(Name , Age, Salary ,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
   # Positional 
   #EmpolyeeInfo("Rahul",26,2000.50,"Pune")  # Correct
   #EmpolyeeInfo(26,"Rahul","Pune",2000.50)  # Wrong
   
   # Keyword Arguments
   EmpolyeeInfo(Age=26,Name="Rahul",City="Pune",Salary=2000.50) # Correct

if __name__ == "__main__":
    main()