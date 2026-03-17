#=====================================================================================================
# CaseStudy Name     : Simple Linear Regression (Manual Implementation)
# Input              : Arrays X and Y, and a value to predict
# Output             : Predicted Y value using regression line
# Description        : Implements Simple Linear Regression from scratch using mean, slope, and intercept
# Author             : Manav Mahadev Jadhav
# Date               : 07/03/2026
#=====================================================================================================

import numpy as np

#-----------------------------------------------------------------------------------------------------
# Function    : SimpleLinearRegression
# Description : Computes slope and intercept using given data and predicts Y for input X
#-----------------------------------------------------------------------------------------------------
def SimpleLinearRegression(X,Y,value):
    print("X = ", X)
    print("Y = ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_bar  = ",mean_x)
    print("Y_bar  = ",mean_y)

    n = len(X)

# Y = mX + C

# m = (summ (X-X_bar) * (Y-Y_bar)) /  (Summ (X -X_bar)**2)   
    numerator = 0 
    denominator = 0
 
    for i in range(n):
        numerator += ((X[i] - mean_x)* (Y[i] - mean_y))
        denominator += ((X[i]- mean_x)**2)

    m = numerator /denominator

    print("Slope of line ie m is : ",m)

    C = mean_y - (m * mean_x)

    print("Y-Intercept of line i.e C : ",C)
    
    Result = m * value + C
    print(f"Predicted Y for {value} is : {Result}")
    
#-----------------------------------------------------------------------------------------------------
# Function    : main
# Description : Driver code to take input and call Simple Linear Regression function
#-----------------------------------------------------------------------------------------------------
def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Enter the value of X that needs to be predicted : ")
    value = int(input())

    SimpleLinearRegression(X,Y,value)

if __name__ == "__main__":
    main()