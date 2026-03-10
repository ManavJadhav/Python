#=====================================================================================================
# CaseStudy Name     : Student Performance Prediction using Decision Tree
# Input              : student_performance_ml.csv
# Output             : Predicted Final Result with Accuracy Score
# Description        : Builds and evaluates a Decision Tree model to predict student performance.
#                      Includes dataset analysis, feature removal experiment, training/testing
#                      accuracy evaluation, prediction results, and confusion matrix visualization.
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
# Description : Calculates training accuracy of the model
# Input       : X_train, Y_train, trained_model
# Output      : TrainingAccuracy
#-----------------------------------------------------------------------------------------------------
def CalculateTrainingAccuracy(X_train, Y_train, trained_model):

    print(Border)
    print("Calculate training accuracy of the Model")
    print(Border)

    TrainPrediction = trained_model.predict(X_train)

    TrainingAccuracy = accuracy_score(Y_train, TrainPrediction)

    print(f"Training Accuracy of the model is : {TrainingAccuracy*100}%")

    return TrainingAccuracy


#-----------------------------------------------------------------------------------------------------
# Function    : ConMatrix
# Description : Displays Confusion Matrix for the model
# Input       : Y_test, Result
# Output      : Confusion matrix plot
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


#-----------------------------------------------------------------------------------------------------
# Function    : CalculateTestingAccuracy
# Description : Calculates testing accuracy of the model
# Input       : Y_test, Result
# Output      : TestingAccuracy
#-----------------------------------------------------------------------------------------------------
def CalculateTestingAccuracy(Y_test, Result):

    print(Border)
    print("Calculate testing accuracy of the Model")
    print(Border)

    TestingAccuracy = accuracy_score(Y_test, Result)

    print(f"Testing Accuracy of the model is : {TestingAccuracy*100}%")

    return TestingAccuracy


#-----------------------------------------------------------------------------------------------------
# Function    : TestModel
# Description : Tests the trained model using the testing dataset
# Input       : X_test, Y_test, trained_model
# Output      : Result
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
        # test_size = 0.3,
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
    print("Visualisation of dataset")
    print(Border)

    sns.pairplot(df, hue="FinalResult")

    plt.show()


#-----------------------------------------------------------------------------------------------------
# Function    : AnalyzeData
# Description : Performs dataset analysis and selects independent & dependent variables
# Input       : df
# Output      : X, Y
#-----------------------------------------------------------------------------------------------------
def AnalyzeData(df):

    print(Border)
    print("Data Analysis")
    print(Border)

    print("Removing SleepHours from dataset")
    df = df.loc[:, df.columns != "SleepHours"]

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
        "AssignmentsCompleted"
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
# Description : Driver Code
#-----------------------------------------------------------------------------------------------------
def main():

    df = Load_Data()

    X, Y = AnalyzeData(df)

    # DatasetVisualisation(df)

    X_train, X_test, Y_train, Y_test = SplittingData(X, Y)

    model = BuildModel()

    trained_model = TrainModel(X_train, Y_train, model)

    print("Importance Score of each feature :", trained_model.feature_importances_)

    Result = TestModel(X_test, Y_test, trained_model)

    TestingAccuracy = CalculateTestingAccuracy(Y_test, Result)

    TrainingAccuracy = CalculateTrainingAccuracy(X_train, Y_train, trained_model)

    ConMatrix(Y_test, Result)


if __name__ == "__main__":
    main()


# After removing SleepHours from the dataset, the accuracy remains the same.
# Hence this feature does not significantly affect the performance of the model.