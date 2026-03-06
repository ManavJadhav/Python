#=====================================================================================================
# CaseStudy Name    : Student Performance Prediction using Decision Tree
# Description       : Builds and evaluates a Decision Tree model to predict student performance
# Input             : student_performance_ml.csv
# Output            : Predicted Final Result with Accuracy Score
# Author            : Manav Mahadev Jadhav
# Date              : 27/02/2026
# Dependencies      : pandas, scikit-learn
#=====================================================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

Border = "-" * 50

#-----------------------------------------------------------------------------------------------------
# Function Name    : train_model
# Description      : Trains the given model using the training dataset.
# Input            : X_train (DataFrame), Y_train (Series), model (sklearn classifier)
# Output           : Trained model
#-----------------------------------------------------------------------------------------------------
def train_model(X_train, Y_train, model):
    print(Border)
    print("Training the Model")
    print(Border)

    trained_model = model.fit(X_train, Y_train)
    print("Model Training Completed")
    return trained_model

#-----------------------------------------------------------------------------------------------------
# Function Name    : build_model
# Description      : Creates a Decision Tree classifier.
# Input            : None
# Output           : DecisionTreeClassifier instance
#-----------------------------------------------------------------------------------------------------
def build_model():
    print(Border)
    print("Building the Model")
    print(Border)

    model = DecisionTreeClassifier()
    print("Model Successfully Created:", model)
    return model

#-----------------------------------------------------------------------------------------------------
# Function Name    : split_data
# Description      : Splits dataset into training and testing sets.
# Input            : X (DataFrame), Y (Series)
# Output           : X_train, X_test, Y_train, Y_test
#-----------------------------------------------------------------------------------------------------
def split_data(X, Y):
    print(Border)
    print("Splitting Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("Y_train:", Y_train.shape)
    print("Y_test :", Y_test.shape)

    return X_train, X_test, Y_train, Y_test

#-----------------------------------------------------------------------------------------------------
# Function Name    : analyze_data
# Description      : Selects independent (features) and dependent (target) variables.
# Input            : df (DataFrame)
# Output           : X (DataFrame), Y (Series)
#-----------------------------------------------------------------------------------------------------
def analyze_data(df):
    print(Border)
    print("Deciding Independent & Dependent Variables")
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
# Description      : Loads the dataset from CSV file.
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
# Description      : Driver function to execute complete workflow: load data, analyze, split, build and train model.
#-----------------------------------------------------------------------------------------------------
def main():
    df = load_data()
    X, Y = analyze_data(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    model = build_model()
    trained_model = train_model(X_train, Y_train, model)

#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()