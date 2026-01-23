#####################################################################################################################
#  Lambda Function  : FilterLambdaLength
#  Input            : list
#  Output           : list
#  Description      : Returns a list of strings whose length is greater than 5 using lambda and filter().
#  Author           : Manav Mahadev Jadhav
#  Date             : 22/01/2026
#####################################################################################################################

# def FilterLambdaLength(strx):
#     return len(strx) > 5

FilterLambdaLength = lambda strx : len(strx) > 5

def main():
    Arr = list()
    Size = 0
    Value = 0

    print("Enter the number of Elements : ")
    Size = int(input())

    print("Enter the Elements : ")
    for i in range(Size):
        Value = input()
        Arr.append(Value)
    
    FData = list(filter(FilterLambdaLength,Arr))

    # FData = list(filter(lambda strx : len(strx) > 5,Arr))
    
    print("Strings having length greater than 5 are :",FData)

if __name__ == "__main__":
    main()