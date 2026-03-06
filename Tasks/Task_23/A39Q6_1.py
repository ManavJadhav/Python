#=====================================================================================================
# CaseStudy Name    : Student Performance Prediction using Decision Tree
# Description       : Builds, trains, tests, evaluates a Decision Tree model and calculates testing accuracy
# Input             : student_performance_ml.csv
# Output            : Predicted Final Result, Testing Accuracy
# Author            : Manav Mahadev Jadhav
# Date              : 27/02/2026
# Dependencies      : pandas, scikit-learn
#=====================================================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Border = "-"*50

#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_testing_accuracy
# Description      : Calculates accuracy on testing dataset
# Input            : Y_test (Series), predictions (array)
# Output           : testing_accuracy (float)
#-----------------------------------------------------------------------------------------------------
def calculate_testing_accuracy(Y_test, predictions):
    print(Border)
    print("Calculate Testing Accuracy of the Model")
    print(Border)   

    testing_accuracy = accuracy_score(Y_test, predictions)
    print(f"Testing Accuracy of the model is: {testing_accuracy*100}%")
    return testing_accuracy

#-----------------------------------------------------------------------------------------------------
# Function Name    : test_model
# Description      : Tests the trained model on X_test and returns predictions
# Input            : X_test (DataFrame), Y_test (Series), trained_model (sklearn classifier)
# Output           : predictions (array)
#-----------------------------------------------------------------------------------------------------
def test_model(X_test, Y_test, trained_model):
    print(Border)
    print("Test the Model")
    print(Border)

    predictions = trained_model.predict(X_test)
    print("Expected Answer  :", list(Y_test))
    print("Predicted Answer :", list(predictions))

    return predictions

#-----------------------------------------------------------------------------------------------------
# Function Name    : train_model
# Description      : Trains the model on X_train and Y_train
# Input            : X_train (DataFrame), Y_train (Series), model (sklearn classifier)
# Output           : trained_model (sklearn classifier)
#-----------------------------------------------------------------------------------------------------
def train_model(X_train, Y_train, model):
    print(Border)
    print("Train the Model")
    print(Border)

    trained_model = model.fit(X_train, Y_train)
    print("Model Training Completed")
    return trained_model

#-----------------------------------------------------------------------------------------------------
# Function Name    : build_model
# Description      : Creates a Decision Tree classifier with max_depth=1
# Input            : None
# Output           : model (DecisionTreeClassifier)
#-----------------------------------------------------------------------------------------------------
def build_model():
    print(Border)
    print("Build the Model")
    print(Border)

    model = DecisionTreeClassifier(max_depth=1)
    print("Model Successfully Created:", model)
    return model

#-----------------------------------------------------------------------------------------------------
# Function Name    : split_data
# Description      : Splits dataset into training and testing sets
# Input            : X (DataFrame), Y (Series)
# Output           : X_train, X_test, Y_train, Y_test
#-----------------------------------------------------------------------------------------------------
def split_data(X, Y):
    print(Border)
    print("Split the Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("Y_train:", Y_train.shape)
    print("Y_test :", Y_test.shape)

    return X_train, X_test, Y_train, Y_test

#-----------------------------------------------------------------------------------------------------
# Function Name    : analyze_data
# Description      : Decides independent (X) and dependent (Y) variables for the model
# Input            : df (DataFrame)
# Output           : X (DataFrame), Y (Series)
#-----------------------------------------------------------------------------------------------------
def analyze_data(df):
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

    print("X (Independent):", X.shape)
    print("Y (Dependent)  :", Y.shape)
    return X, Y

#-----------------------------------------------------------------------------------------------------
# Function Name    : load_data
# Description      : Loads dataset from CSV
# Input            : None
# Output           : df (DataFrame)
#-----------------------------------------------------------------------------------------------------
def load_data():
    Dataset_Name = "student_performance_ml.csv"
    print(Border)
    df = pd.read_csv(Dataset_Name)
    print("Dataset Loaded Successfully")
    print(Border)
    return df

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Driver function to execute full workflow
#-----------------------------------------------------------------------------------------------------
def main():
    df = load_data()
    X, Y = analyze_data(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    model = build_model()
    trained_model = train_model(X_train, Y_train, model)
    predictions = test_model(X_test, Y_test, trained_model)
    testing_accuracy = calculate_testing_accuracy(Y_test, predictions)

    # Observations:
    # If max_depth = 1 & test_size = 0.2 => Testing Accuracy ~ 100%
    # If max_depth = 1 & test_size = 0.5 => Testing Accuracy ~ 93.3%