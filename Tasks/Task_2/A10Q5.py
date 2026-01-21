###########################################################################
#  Function name :     FindOdd
#  Input :             int 
#  Output :            list
#  Description :       It used to return all odd numbers till that number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def FindOdd(No):
    
    Result = []

    for i in range(1,No+1):
        if((i % 2)==1):
            Result.append(i)
    
    return Result


def main():

    Value = 0
    Ret = None

    print("Enter a number: ")
    Value = int(input())

    Ret = FindOdd(Value)
    print(Ret)

if __name__ == "__main__":
    main()