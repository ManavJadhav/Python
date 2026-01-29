######################################################################################################
# Program Name     : NumberAnalysis
# Input            : Integer number
# Output           : Displays whether the number is prime and perfect,
#                    prints all factors, and prints sum of factors
# Description      : Demonstrates object-oriented programming by performing
#                    number-related operations such as prime check,
#                    factor generation, sum of factors, and perfect number check.
# Author           : Manav Mahadev Jadhav
# Date             : 27/01/2026
######################################################################################################

class Numbers:

    def __init__(self,A):
        self.Value =  A

    def ChkPrime(self):
        if(self.Value < 2 ):
            return False

        for i in range(2,self.Value):
            if (self.Value % i == 0 ):
                return False
        
        return True
    
    def Factors(self):

        for i in range(1,self.Value):
            if (self.Value % i == 0 ):
                print(i)
        print(self.Value)
    
    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value):
            if (self.Value % i == 0 ):
                Sum += i
        return Sum

    def ChkPerfect(self):
        flag = False
        bRet = self.SumFactors()
        if(bRet == self.Value):
            flag =  True
        return flag
    
def main():
    No = 0 

    print("Enter a number : ")
    No=int(input())

    obj1 = Numbers(No)

    Ret = obj1.ChkPrime()
    if(Ret == True):
        print("It is a Prime Number ")
    else:
        print("It is a NOT Prime Number ")

    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print("It is a Perfect Number ")
    else:
        print("It is a NOT Perfect Number ")

    obj1.Factors()

    Ret = obj1.SumFactors()
    print("Summation of Factors is : ",Ret + No)
    

if __name__ == "__main__":
    main()