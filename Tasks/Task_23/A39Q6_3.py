#=====================================================================================================
# CaseStudy Name    : Student Performance Prediction using Decision Tree
# Input             : student_performance_ml.csv
# Output            : Predicted Final Result with Accuracy Score
# Description       : Builds, trains, tests, and evaluates a Decision Tree model to predict student
#                     performance. Calculates testing accuracy and displays expected vs predicted results.
# Author            : Manav Mahadev Jadhav
# Date              : 27/02/2026
# Dependencies      : pandas, scikit-learn, matplotlib
#=====================================================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

Border = "-"*50

#-----------------------------------------------------------------------------------------------------
# Function    : CalculateTestingAccuracy
# Description : Calculates and prints testing accuracy of the model
# Input       : Y_test (Series), Result (array)
# Output      : TestingAccuracy (float)
#-----------------------------------------------------------------------------------------------------
def CalculateTestingAccuracy(Y_test, Result):
    print(Border)
    print("Calculate Testing Accuracy of the Model")
    print(Border)   

    TestingAccuracy = accuracy_score(Y_test, Result)
    print(f"Testing Accuracy of the model is : {TestingAccuracy*100}%")
    return TestingAccuracy

#-----------------------------------------------------------------------------------------------------
# Function    : TestModel
# Description : Tests the trained model on X_test and returns predictions
# Input       : X_test (DataFrame), Y_test (Series), trained_model (DecisionTreeClassifier)
# Output      : Result (array)
#-----------------------------------------------------------------------------------------------------
def TestModel(X_test, Y_test, trained_model):
    print(Border)
    print("Test the Model")
    print(Border)

    Result = trained_model.predict(X_test)
    print("Expected Answer  :", list(Y_test))
    print("Predicted Answer :", list(Result))
    return Result

#-----------------------------------------------------------------------------------------------------
# Function    : TrainModel
# Description : Trains the model using X_train and Y_train and returns trained model
# Input       : X_train (DataFrame), Y_train (Series), model (DecisionTreeClassifier)
# Output      : trained_model
#-----------------------------------------------------------------------------------------------------
def TrainModel(X_train, Y_train, model):
    print(Border)
    print("Train the Model")
    print(Border)

    trained_model = model.fit(X_train, Y_train)
    print("Model Training Completed")
    return trained_model

#-----------------------------------------------------------------------------------------------------
# Function    : BuildModel
# Description : Builds a Decision Tree model with max_depth=None and returns it
# Input       : None
# Output      : model (DecisionTreeClassifier)
#-----------------------------------------------------------------------------------------------------
def BuildModel():
    print(Border)
    print("Build the Model")
    print(Border)

    model = DecisionTreeClassifier(max_depth=None)
    print("Model Successfully Created :", model)
    return model

#-----------------------------------------------------------------------------------------------------
# Function    : SplittingData
# Description : Splits dataset into training and testing sets
# Input       : X (DataFrame), Y (Series)
# Output      : X_train, X_test, Y_train, Y_test
#-----------------------------------------------------------------------------------------------------
def SplittingData(X, Y):
    print(Border)
    print("Split the Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )
    print("X_train :", X_train.shape)
    print("X_test  :", X_test.shape)
    print("Y_train :", Y_train.shape)
    print("Y_test  :", Y_test.shape)
    return X_train, X_test, Y_train, Y_test

#-----------------------------------------------------------------------------------------------------
# Function    : AnalyzeData
# Description : Determines independent (X) and dependent (Y) variables
# Input       : df (DataFrame)
# Output      : X (DataFrame), Y (Series)
#-----------------------------------------------------------------------------------------------------
def AnalyzeData(df):
    print(Border)
    print("Decide Independent & Dependent Variables")
    print(Border)

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
    X = df[feature_cols]
    Y = df["FinalResult"]

    print("X (Independent) :", X.shape)
    print("Y (Dependent)   :", Y.shape)
    return X, Y

#-----------------------------------------------------------------------------------------------------
# Function    : Load_Data
# Description : Loads dataset from CSV and returns as DataFrame
# Input       : None
# Output      : df (DataFrame)
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    print(Border)
    df = pd.read_csv(Dataset_Name)
    print("Dataset Loaded Successfully")
    print(Border)
    return df

#-----------------------------------------------------------------------------------------------------
# Function    : main
# Description : Driver code to run the complete case study workflow
#-----------------------------------------------------------------------------------------------------
def main():
    df = Load_Data()
    X, Y = AnalyzeData(df)
    X_train, X_test, Y_train, Y_test = SplittingData(X, Y)
    model = BuildModel()
    trained_model = TrainModel(X_train, Y_train, model)
    Result = TestModel(X_test, Y_test, trained_model)
    TestingAccuracy = CalculateTestingAccuracy(Y_test, Result)

    # Observations:
    # If max_depth = None & test_size = 0.2 => TestingAccuracy is 100%
    # If max_depth = None & test_size = 0.5 => TestingAccuracy is 93.3%

if __name__ == "__main__":
    main()