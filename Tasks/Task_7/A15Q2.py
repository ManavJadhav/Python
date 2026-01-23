######################################################################################################
#  Lambda Function  : FilterLambdaEven
#  Input            : list
#  Output           : list
#  Description      : Returns a list containing even numbers using lambda and filter().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

# def FilterLambdaEven(No):
#     return (No % 2 == 0)

FilterLambdaEven = lambda No : (No % 2 == 0)

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
    
    FData = list(filter(FilterLambdaEven,Arr))

    #FData = list(filter(lambda No : (No % 2 == 0),Arr))

    print("The Even numbers from list are : ",FData)

if __name__ == "__main__":
    main()