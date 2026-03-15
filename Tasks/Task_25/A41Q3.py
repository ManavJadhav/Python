#=====================================================================================================
# CaseStudy Name     : Student Performance Classification using K-Nearest Neighbors (Manual KNN)
# Input              : X and Y coordinates representing student features
# Output             : Predicted class (Pass / Fail)
# Description        : Implements the K-Nearest Neighbors algorithm manually using Euclidean Distance
# Author             : Manav Mahadev Jadhav
# Date               : 05/03/2026
#=====================================================================================================

import math

def FindNearest(sorted_data):
    Border = "-"*40
    print(Border)
    print("Enter the value of  K : ")
    k = int(input())
    print(Border)
    nearest = sorted_data[:k]

    for d in nearest:
        print(d)

    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1
    print(Border)
    print("Voting Result is : ")

    for d in votes:
        print("Name : ",d, "Number of votes : ",votes[d])
    print(Border)

    predicted_class = max(votes,key=votes.get)

    return predicted_class

# _/ (X2 - X1)**2 + (Y2-Y1)**2
def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y']- P2['Y'])**2 )
    return Ans


def KNeighborsClassifierX(new_point):
    Border = "-"*40

    data = [
            {'point':'A','X':2, 'Y':60 ,'label' :'Fail'},
            {'point':'B','X':5, 'Y':80 ,'label' :'Pass'},
            {'point':'C','X':6, 'Y':85 ,'label' :'Pass'},
            {'point':'D','X':1, 'Y':50 ,'label' :'Fail'}
           ]
    
    for d in data : 
        d['distance'] = EucDistance(d,new_point)
    print(Border)
    print("Distance of each ponit from new_point is : ")
    for d in data :
        print(d)
    print(Border)

    sorted_data = sorted(data,key=lambda x : x['distance'])
    print(Border)
    print("Sorted data is  :")
    for d in data :
        print(d)
    print(Border)

    print(Border)
    Result = FindNearest(sorted_data)
    print(f"Predicted class of {new_point} is : {Result}")
    print(Border)

#-----------------------------------------------------------------------------------------------------
# Function    : main
# Description : Driver Code
#-----------------------------------------------------------------------------------------------------
def main():
    Border = "-"*40

    keys = ['X','Y']
    arr = {}
    print(Border)
    print("Enter X and Y coordinates: ")

    for key in keys:
        value = int(input(f"Enter a value for {key}:"))
        arr[key] = value

    print("The new coordinates are : ")
    for i in arr:
     print(f"{i} : {arr[i]}")
    print(Border)

    KNeighborsClassifierX(arr)

if __name__ == "__main__":
    main()