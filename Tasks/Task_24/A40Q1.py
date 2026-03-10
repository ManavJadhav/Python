#=====================================================================================================
# CaseStudy Name     : Student Performance Prediction using Decision Tree
# Input              : student_performance_ml.csv
# Output             : Predicted Final Result with Accuracy Score
# Description        : Builds and evaluates a Decision Tree model to predict student performance.
#                      Includes dataset analysis, model training, prediction, accuracy evaluation,
#                      feature importance extraction, and confusion matrix visualization.
# Author             : Manav Mahadev Jadhav
# Date               : 27/02/2026
#=====================================================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-" * 50


#-----------------------------------------------------------------------------------------------------
# Function    : CalculateTrainingAccuracy
# Description : Calculates the training accuracy of the trained model
# Input       : X_train, Y_train, trained_model
# Output      : TrainingAccuracy
#-----------------------------------------------------------------------------------------------------
def CalculateTrainingAccuracy(X_train, Y_train, trained_model):

    print(Border)
    print("Calculate Training Accuracy of the Model")
    print(Border)

    TrainPrediction = trained_model.predict(X_train)

    TrainingAccuracy = accuracy_score(Y_train, TrainPrediction)

    print(f"Training Accuracy of the model is : {TrainingAccuracy*100}%")

    return TrainingAccuracy


#-----------------------------------------------------------------------------------------------------
# Function    : ConMatrix
# Description : Displays the Confusion Matrix for model predictions
# Input       : Y_test, Result
# Output      : Displays confusion matrix plot
#-----------------------------------------------------------------------------------------------------
def ConMatrix(Y_test, Result):

    print(Border)
    print("Display Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test, Result)

    print("Confusion Matrix :")
    print(cm)

    data = ConfusionMatrixDisplay(confusion_matrix=cm)
    data.plot()

    plt.title("Confusion Matrix of Student Performance")
    plt.show()

    # 1 (Pass) : Positive
    # 0 (Fail) : Negative

    # True  Positive : Actual Pass Predicted Pass
    # True  Negative : Actual Fail Predicted Fail
    # False Positive : Actual Fail Predicted Pass
    # False Negative : Actual Pass Predicted Fail


#-----------------------------------------------------------------------------------------------------
# Function    : CalculateTestingAccuracy
# Description : Calculates the testing accuracy of the trained model
# Input       : Y_test, Result
# Output      : TestingAccuracy
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
# Description : Tests the trained model on testing dataset
# Input       : X_test, Y_test, trained_model
# Output      : Result (Predicted values)
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
# Description : Trains the Decision Tree model
# Input       : X_train, Y_train, model
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
# Description : Builds the Decision Tree model
# Input       : None
# Output      : model
#-----------------------------------------------------------------------------------------------------
def BuildModel():

    print(Border)
    print("Build the Model")
    print(Border)

    model = DecisionTreeClassifier()

    print("Model Successfully Created :", model)

    return model


#-----------------------------------------------------------------------------------------------------
# Function    : SplittingData
# Description : Splits dataset into training and testing dataset
# Input       : X, Y
# Output      : X_train, X_test, Y_train, Y_test
#-----------------------------------------------------------------------------------------------------
def SplittingData(X, Y):

    print(Border)
    print("Split the Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        # test_size = 0.2,
        random_state = 42
    )

    print("X_train :", X_train.shape)
    print("X_test  :", X_test.shape)
    print("Y_train :", Y_train.shape)
    print("Y_test  :", Y_test.shape)

    return X_train, X_test, Y_train, Y_test


#-----------------------------------------------------------------------------------------------------
# Function    : DatasetVisualisation
# Description : Visualizes dataset using pairplot
# Input       : df
# Output      : Pairplot graph
#-----------------------------------------------------------------------------------------------------
def DatasetVisualisation(df):

    print(Border)
    print("Visualisation of Dataset")
    print(Border)

    sns.pairplot(df, hue="FinalResult")

    plt.show()


#-----------------------------------------------------------------------------------------------------
# Function    : AnalyzeData
# Description : Performs dataset analysis and selects independent and dependent variables
# Input       : df
# Output      : X, Y
#-----------------------------------------------------------------------------------------------------
def AnalyzeData(df):

    print(Border)
    print("Data Analysis")
    print(Border)

    print("Shape of dataset :", df.shape)
    print("Column Names :", list(df.columns))

    print("Missing Values (Per Column)")
    print(df.isnull().sum())

    print("Statistical report of dataset")
    print(df.describe())

    print("Decide Independent & Dependent Variables")

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
# Description : Loads dataset from CSV file
# Input       : None
# Output      : df
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
# Description : Driver function that executes the entire workflow
#-----------------------------------------------------------------------------------------------------
def main():

    df = Load_Data()

    X, Y = AnalyzeData(df)

    # DatasetVisualisation(df)

    X_train, X_test, Y_train, Y_test = SplittingData(X, Y)

    model = BuildModel()

    trained_model = TrainModel(X_train, Y_train, model)

    model_featureimp = trained_model.feature_importances_

    print("Importance Score of each feature :", model_featureimp)

    # The feature which contributes the most in predicting FinalResult is Attendance.
    # While other features such as StudyHours, PreviousScore, AssignmentsCompleted,
    # SleepHours contribute the least.

    Result = TestModel(X_test, Y_test, trained_model)

    TestingAccuracy = CalculateTestingAccuracy(Y_test, Result)

    TrainingAccuracy = CalculateTrainingAccuracy(X_train, Y_train, trained_model)

    ConMatrix(Y_test, Result)


#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()