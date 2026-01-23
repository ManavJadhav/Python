######################################################################################################
#  Lambda Function  : FilterLambdaOdd
#  Input            : list
#  Output           : list
#  Description      : Returns a list containing odd numbers using lambda and filter().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

# def FilterLambdaOdd(No):
#     return (No % 2 != 0)

FilterLambdaOdd = lambda No : (No % 2 != 0)

def main():
    Arr = list()
    Size = 0
    Value = 0

    print("Enter the number of Elements : ")
    Size = int(input())

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)
    
    FData = list(filter(FilterLambdaOdd,Arr))

    #FData = list(filter(lambda No : (No % 2 != 0),Arr))

    print("The Odd numbers from list are : ",FData)

if __name__ == "__main__":
    main()