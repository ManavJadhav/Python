def EmpolyeeInfo(Name , Age, Salary ,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
   # Keyword Arguments
   EmpolyeeInfo(Age=26,Name="Rahul",City="Pune",Salary=None) # Correct

if __name__ == "__main__":
    main()