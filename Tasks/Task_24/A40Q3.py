#=====================================================================================================
# CaseStudy Name     : Student Performance Prediction using Decision Tree
# Input              : student_performance_ml.csv
# Output             : Predicted Final Result with Accuracy Score
# Description        : Builds and evaluates a Decision Tree model to predict student performance
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
# Description : This function is used to calculate training accuracy of the model
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
# Description : This function is used to display Confusion Matrix
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

    # True Positive  : Actual Pass Predicted Pass
    # True Negative  : Actual Fail Predicted Fail
    # False Positive : Actual Fail Predicted Pass
    # False Negative : Actual Pass Predicted Fail


#-----------------------------------------------------------------------------------------------------
# Function    : CalculateTestingAccuracy
# Description : This function is used to calculate testing accuracy of the model
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
# Description : This function is used to test the model
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
# Description : This function is used to train the model
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
# Description : This function is used to build the model
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
# Description : This function is used to split data into training and testing dataset
#-----------------------------------------------------------------------------------------------------
def SplittingData(X, Y):

    print(Border)
    print("Split the Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        # test_size = 0.7,
        random_state = 42
    )

    print("X_train :", X_train.shape)
    print("X_test  :", X_test.shape)
    print("Y_train :", Y_train.shape)
    print("Y_test  :", Y_test.shape)

    return X_train, X_test, Y_train, Y_test


#-----------------------------------------------------------------------------------------------------
# Function    : DatasetVisualisation
# Description : This function is used to visualize dataset
#-----------------------------------------------------------------------------------------------------
def DatasetVisualisation(df):

    print(Border)
    print("Visualisation of dataset")
    print(Border)

    sns.pairplot(df, hue="FinalResult")

    plt.show()


#-----------------------------------------------------------------------------------------------------
# Function    : AnalyzeData
# Description : This function is used to decide independent & dependent variables
#-----------------------------------------------------------------------------------------------------
def AnalyzeData(df):

    print(Border)
    print("Data Analysis")
    print(Border)

    print("Keeping only 2 features StudyHours & Attendance")

    df = df[["StudyHours", "Attendance", "FinalResult"]]

    print("Shape of dataset :", df.shape)
    print("Column Names :", list(df.columns))

    print("Missing Values (Per Column)")
    print(df.isnull().sum())

    print("Statistical report of dataset")
    print(df.describe())

    print("Decide Independent & Dependent Variables")

    feature_cols = [
        "StudyHours",
        "Attendance"
    ]

    X = df[feature_cols]
    Y = df["FinalResult"]

    print("X (Independent) :", X.shape)
    print("Y (Dependent)   :", Y.shape)

    return X, Y


#-----------------------------------------------------------------------------------------------------
# Function    : Load_Data
# Description : This function is used to load the dataset
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


# By training the model using only StudyHours and Attendance, the accuracy remains the same.
# Hence removing other features does not significantly affect the model performance.