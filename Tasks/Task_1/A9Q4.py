
###########################################################################
#  Function name :     ChkCube
#  Input :             int 
#  Output :            int
#  Description :       It used to find cube of a number .
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkCube(No):
    
    iCube = 0
    
    iCube = No ** 3
    
    return iCube


def main():

    Value = 0
    Ret = 0

    print("Enter a number: ")
    Value = int(input())

    Ret = ChkCube(Value)
    print(f"Cube of {Value}  is : ",Ret)

if __name__ == "__main__":
    main()