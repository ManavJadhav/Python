# =====================================================================================================
# Case Study Name  : K-Nearest Neighbors Classification (Manual Implementation)
# Input            : X and Y coordinates from user
# Output           : Predicted class using different K values
# Description      : Implements KNN algorithm manually using Euclidean distance and majority voting
# Author           : Manav Mahadev Jadhav
# Date             : 05/03/2026
# =====================================================================================================

import math


# -----------------------------------------------------------------------------------------------------
# Function Name : FindNearest
# Description   : Finds K nearest neighbours and performs voting
# -----------------------------------------------------------------------------------------------------
def FindNearest(sorted_data, k):

    Border = "-" * 40

    nearest = sorted_data[:k]

    print(f"Nearest {k} neighbors:")
    for d in nearest:
        print(d)

    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label, 0) + 1

    print(Border)
    print("Voting Result is:")

    for label, count in votes.items():
        print(f"Name : {label} | Number of votes : {count}")

    print(Border)

    predicted_class = max(votes, key=votes.get)

    return predicted_class


# -----------------------------------------------------------------------------------------------------
# Function Name : EucDistance
# Description   : Calculates Euclidean distance between two points
# Formula       : √((X2 - X1)^2 + (Y2 - Y1)^2)
# -----------------------------------------------------------------------------------------------------
def EucDistance(P1, P2):

    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans


# -----------------------------------------------------------------------------------------------------
# Function Name : KNeighborsClassifier
# Description   : Applies KNN classification on the given point
# -----------------------------------------------------------------------------------------------------
def KNeighborsClassifier(new_point):

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
    print("Distance of each point from new_point is:")

    for d in data:
        print(d)

    print(Border)

    sorted_data = sorted(data, key=lambda x: x['distance'])

    print("Sorted data is:")

    for d in sorted_data:
        print(d)

    print(Border)

    k_values = [1, 3, 5]
    results = []

    for k in k_values:
        res = FindNearest(sorted_data, k)
        results.append(res)

    print(Border)

    for i in range(len(k_values)):
        print(f"Predicted class of {new_point} with k={k_values[i]} is: {results[i]}")

    print(Border)


# -----------------------------------------------------------------------------------------------------
# Function Name : main
# Description   : Driver code
# -----------------------------------------------------------------------------------------------------
def main():

    Border = "-" * 40

    keys = ['X', 'Y']
    new_point = {}

    print(Border)
    print("Enter X and Y coordinates:")

    for key in keys:
        value = int(input(f"Enter a value for {key}: "))
        new_point[key] = value

    print("The new coordinates are:")

    for k, v in new_point.items():
        print(f"{k} : {v}")

    print(Border)

    KNeighborsClassifier(new_point)


if __name__ == "__main__":
    main()