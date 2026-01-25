######################################################################################################
#  Function Name          : ListPrime
#  Input                  : list
#  Output                 : int
#  Description            : Returns the addition of all prime numbers from the list.
#  Author                 : Manav Mahadev Jadhav
#  Date                   : 23/01/2026
######################################################################################################

from MarvellousNum import ChkPrime

def ListPrime(Brr):

    Result = False
    Sum = 0

    Result = list(filter(ChkPrime,Brr))
    print(Result)
    for i in Result:
        Sum += i

    return Sum

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


    Ret = ListPrime(Arr)
    print(Ret)
    

if __name__ == "__main__":
    main()