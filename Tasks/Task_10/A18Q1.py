######################################################################################################
#  Function Name          : Addition
#  Input                  : list
#  Output                 : int
#  Description            : Returns the addition of all elements from the list.
#  Author                 : Manav Mahadev Jadhav
#  Date                   : 23/01/2026
######################################################################################################

def Addition(Brr):
    Result = 0

    for i in range(len(Brr)):
        Result +=Brr[i]
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

    Ret = Addition(Arr)
    print("Addition is : ",Ret)
    

if __name__ == "__main__":
    main()