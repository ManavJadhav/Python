###########################################################################
#  Function name :     FactorialX
#  Input :             int 
#  Output :            int
#  Description :       It used to find factorial of a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def FactorialX(No):
    
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i    
    
    return Fact


def main():

    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = FactorialX(Value)
    print(Ret)

if __name__ == "__main__":
    main()