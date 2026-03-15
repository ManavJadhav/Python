#=====================================================================================================
# CaseStudy Name     : K-Nearest Neighbors Classification (Manual Implementation)
# Input              : X and Y coordinates from user
# Output             : Predicted class based on nearest neighbors
# Description        : Implements KNN algorithm manually using Euclidean Distance
# Author             : Manav Mahadev Jadhav
# Date               : 05/03/2026
#=====================================================================================================

import math


#-----------------------------------------------------------------------------------------------------
# Function    : FindNearest
# Description : Finds K nearest neighbours and performs voting
#-----------------------------------------------------------------------------------------------------
def FindNearest(sorted_data):

    Border = "-" * 40

    print(Border)
    print("Enter the value of K : ")
    k = int(input())
    print(Border)

    nearest = sorted_data[:k]

    print("Nearest Neighbours : ")
    for d in nearest:
        print(d)

    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    print(Border)
    print("Voting Result is : ")

    for label in votes:
        print("Name :", label, "Number of votes :", votes[label])

    print(Border)

    predicted_class = max(votes, key=votes.get)

    return predicted_class


#-----------------------------------------------------------------------------------------------------
# Function    : EucDistance
# Description : Calculates Euclidean distance between two points
# Formula     : √((X2 - X1)^2 + (Y2 - Y1)^2)
#-----------------------------------------------------------------------------------------------------
def EucDistance(P1, P2):

    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans


#-----------------------------------------------------------------------------------------------------
# Function    : KNeighborsClassifierX
# Description : Applies KNN classification on the given point
#-----------------------------------------------------------------------------------------------------
def KNeighborsClassifierX(new_point):

    Border = "-" * 40

    data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print(Border)
    print("Distance of each point from new_point is :")

    for d in data:
        print(d)

    print(Border)

    sorted_data = sorted(data, key=lambda x: x['distance'])

    print("Sorted data based on distance :")

    for d in sorted_data:
        print(d)

    print(Border)

    Result = FindNearest(sorted_data)

    print(f"Predicted class of {new_point} is : {Result}")

    print(Border)


#-----------------------------------------------------------------------------------------------------
# Function    : main
# Description : Driver Code
#-----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 40

    keys = ['X', 'Y']
    arr = {}

    print(Border)
    print("Enter X and Y coordinates : ")

    for key in keys:
        value = int(input(f"Enter a value for {key} : "))
        arr[key] = value

    print("The new coordinates are :")

    for i in arr:
        print(f"{i} : {arr[i]}")

    print(Border)

    KNeighborsClassifierX(arr)


if __name__ == "__main__":
    main()

