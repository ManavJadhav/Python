######################################################################################################
#  Lambda Function  : FilterLambdaDivisible
#  Input            : list
#  Output           : list
#  Description      : Returns a list of numbers divisible by both 3 and 5 using lambda and filter().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

# def FilterLambdaDivisible(No):
#     return (No % 3 == 0) and (No % 5 == 0)

FilterLambdaDivisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

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
    
    FData = list(filter(FilterLambdaDivisible,Arr))

    #FData = list(filter(lambda No : (No % 3 == 0) and (No % 5 == 0),Arr))

    print("Numbers which are divisible by 3 & 5 are : ",FData)

if __name__ == "__main__":
    main()