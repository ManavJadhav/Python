#=====================================================================================================
# CaseStudy Name    : Student Performance Prediction using Decision Tree
# Description       : Builds, trains, tests, evaluates a Decision Tree model and displays Confusion Matrix
# Input             : student_performance_ml.csv
# Output            : Predicted Final Result, Accuracy Score, Confusion Matrix Plot
# Author            : Manav Mahadev Jadhav
# Date              : 27/02/2026
# Dependencies      : pandas, scikit-learn, matplotlib
#=====================================================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

Border = "-" * 50

#-----------------------------------------------------------------------------------------------------
# Function Name    : display_confusion_matrix
# Description      : Displays confusion matrix for the predictions
# Input            : Y_test (Series), predictions (array)
# Output           : Plots Confusion Matrix
#-----------------------------------------------------------------------------------------------------
def display_confusion_matrix(Y_test, predictions):
    print(Border)
    print("Display Confusion Matrix")
    print(Border) 

    cm = confusion_matrix(Y_test, predictions)
    print("Confusion Matrix:")
    print(cm)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title("Confusion Matrix of Student Performance")
    plt.show()

    # 1 (Pass) : Positive
    # 0 (Fail) : Negative
    # True Positive : Actual Pass Predicted Pass
    # True Negative : Actual Fail Predicted Fail
    # False Positive : Actual Fail Predicted Pass
    # False Negative : Actual Pass Predicted Fail

#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_accuracy
# Description      : Computes the accuracy of the model predictions
# Input            : Y_test (Series), predictions (array)
# Output           : Accuracy (float)
#-----------------------------------------------------------------------------------------------------
def calculate_accuracy(Y_test, predictions):
    print(Border)
    print("Calculate Accuracy of the Model")
    print(Border)   

    accuracy = accuracy_score(Y_test, predictions)
    print(f"Accuracy of the model is: {accuracy * 100}%")
    return accuracy

#-----------------------------------------------------------------------------------------------------
# Function Name    : test_model
# Description      : Tests the trained model and prints predictions vs actual results
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
# Description      : Trains the given model using the training dataset
# Input            : X_train (DataFrame), Y_train (Series), model (sklearn classifier)
# Output           : trained_model
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
# Description      : Creates a Decision Tree classifier
# Input            : None
# Output           : model (DecisionTreeClassifier)
#-----------------------------------------------------------------------------------------------------
def build_model():
    print(Border)
    print("Build the Model")
    print(Border)

    model = DecisionTreeClassifier()
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
# Description      : Selects independent (features) and dependent (target) variables
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
# Description      : Loads the dataset from CSV file
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
# Description      : Driver function to execute complete workflow: load data, analyze, split, build, train, test, calculate accuracy, and display confusion matrix
#-----------------------------------------------------------------------------------------------------
def main():
    df = load_data()
    X, Y = analyze_data(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    model = build_model()
    trained_model = train_model(X_train, Y_train, model)
    predictions = test_model(X_test, Y_test, trained_model)
    accuracy = calculate_accuracy(Y_test, predictions)
    display_confusion_matrix(Y_test, predictions)

#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()