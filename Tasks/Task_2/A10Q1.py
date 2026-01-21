###########################################################################
#  Function name :     TableNum
#  Input :             int 
#  Output :            list
#  Description :       It used to display multiplication table of a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def TableNum(No):
    
    Result = []
    Mult = 0

    for i in range(1,11):
        Mult = No * i
        Result.append(Mult)
    
    return Result


def main():

    Value = 0
    Ret = None

    print("Enter a number: ")
    Value = int(input())

    Ret = TableNum(Value)
    print(Ret)

if __name__ == "__main__":
    main()