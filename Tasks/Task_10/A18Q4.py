######################################################################################################
#  Function Name          : ElementFreq
#  Input                  : list
#  Output                 : int
#  Description            : Returns the frequency of element given by the user from the list.
#  Author                 : Manav Mahadev Jadhav
#  Date                   : 23/01/2026
######################################################################################################

def ElementFreq(Brr,No):
    Result = 0

    for i in range(len(Brr)):
        if(Brr[i] == No):
            Result += 1 

    return Result 


def main():
    Arr = list()
    Size = 0
    Value1 = 0
    Value2 = 0
    Ret = 0
    

    print("Enter the number of Elements : ")
    Size = int(input())

    print("Enter the Elements : ")
    for i in range(Size):
        Value1 = int(input())
        Arr.append(Value1)

    print("Enter the number you want to search : ")
    Value2 = int(input())

    Ret = ElementFreq(Arr,Value2)
    print(f"Frquency of number {Value2} is : ",Ret)
    

if __name__ == "__main__":
    main()