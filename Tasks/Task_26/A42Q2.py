#=====================================================================================================
# CaseStudy Name     : Simple Linear Regression with Performance Metrics (Manual Implementation)
# Input              : Arrays X and Y
# Output             : Regression parameters, predicted values, R² score, and MSE
# Description        : Implements Simple Linear Regression from scratch and evaluates model using R² and MSE
# Author             : Manav Mahadev Jadhav
# Date               : 05/03/2026
#=====================================================================================================

import numpy as np

#-----------------------------------------------------------------------------------------------------
# Function    : SimpleLinearRegression
# Description : Computes slope and intercept, predicts values, and evaluates model using R² and MSE
#-----------------------------------------------------------------------------------------------------
def SimpleLinearRegression(X,Y):
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
    
    # R**2 = ((summ (Yp-Ybar)**2 / (Y-Y_bar)**2 )
    # MSE = (summ(Y-Yp)**2)
    # Yp = m * X + C
    numerator = 0 
    denominator = 0
    R2 = 0
    nume_mse =0

    for i in range(n) :
        Yp = m * X[i] + C
        print(f"Predicted Y for {X[i]} is : {Yp}")
        numerator += ((Yp - mean_y)**2)
        denominator += ((Y[i]-mean_y)**2)
        nume_mse  += ((Y[i] - Yp)**2)
    
    R2 = numerator / denominator
    print("R**2 Score : ",R2)

    MSE = nume_mse /n

    print("MSE is  : ",MSE)
    
#-----------------------------------------------------------------------------------------------------
# Function    : main
# Description : Driver code to execute regression and evaluation
#-----------------------------------------------------------------------------------------------------
def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]


    SimpleLinearRegression(X,Y)

if __name__ == "__main__":
    main()