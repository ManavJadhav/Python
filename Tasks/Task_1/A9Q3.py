
###########################################################################
#  Function name :     ChkSquare
#  Input :             int 
#  Output :            int
#  Description :       It used to find square of a number .
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkSquare(No):
    
    iSqaure = 0
    
    iSqaure = No ** 2
    
    return iSqaure


def main():

    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = ChkSquare(Value)
    print(f"Square of {Value}  is : ",Ret)

if __name__ == "__main__":
    main()