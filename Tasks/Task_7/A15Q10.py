######################################################################################################
#  Program          : FilterLambdaCount
#  Input            : list
#  Output           : int
#  Description      : Returns the count of even numbers using lambda and filter().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

# def FilterLambdaCount(No):
#     return len(No % 2 == 0)

# FilterLambdaCount = lambda No : (No % 2 == 0)

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
    
    # FData = len(list(filter(FilterLambdaCount,Arr)))

    FData = len(list(filter(lambda No : (No % 2 == 0),Arr)))

    print("Count of Even number is : ",FData)

if __name__ == "__main__":
    main()

# def FilterLambdaCount(No):
#     return len(No % 2 == 0)

# FilterLambdaCount = lambda No : (No % 2 == 0)

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
    
    # FData = len(list(filter(FilterLambdaCount,Arr)))

    FData = len(list(filter(lambda No : (No % 2 == 0),Arr)))

    print("Count of Even number is : ",FData)

if __name__ == "__main__":
    main()