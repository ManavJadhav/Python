######################################################################################################
#  Lambda Function  : MapLambdaSquare
#  Input            : list
#  Output           : list
#  Description      : Returns a list containing squares of all numbers using lambda and map().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
######################################################################################################

# def MapLambdaSquare(No):
#     return No ** 2

MapLambdaSquare = lambda No : No ** 2

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
    
    MData = list(map(MapLambdaSquare,Arr))

    #MData = list(map(lambda No : No ** 2,Arr))

    print("Sqaure of each number from list is : ",MData)

if __name__ == "__main__":
    main()