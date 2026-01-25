######################################################################################################
#  Function Name          : MaximumX
#  Input                  : list
#  Output                 : int
#  Description            : Returns the maximum element from the list.
#  Author                 : Manav Mahadev Jadhav
#  Date                   : 23/01/2026
######################################################################################################

def MaximumX(Brr):
    Result = 0

    for i in range(len(Brr)):
        if(Brr[i] > Result ):
            Result = Brr[i]

    return Result 


def main():
    Arr = list()
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of Elements : ")
    Size = int(input())

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    Ret = MaximumX(Arr)
    print("Maximum number is : ",Ret)
    

if __name__ == "__main__":
    main()