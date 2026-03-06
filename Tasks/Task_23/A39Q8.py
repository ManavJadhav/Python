#=====================================================================================================
# CaseStudy Name    : Student Performance Prediction using Decision Tree
# Description       : Builds and evaluates a Decision Tree model to predict student performance.
#                     Includes data analysis, visualization, training/testing, accuracy calculation,
#                     confusion matrix display, and custom input prediction.
# Input             : student_performance_ml.csv
# Output            : Predicted Final Result for custom input, training/testing accuracy, confusion matrix
# Author            : Manav Mahadev Jadhav
# Date              : 27/02/2026
# Dependencies      : pandas, scikit-learn, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-" * 50

#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_training_accuracy
# Description      : Calculates and prints training accuracy for the trained model
# Input            : X_train (DataFrame), Y_train (Series), trained_model (sklearn classifier)
# Output           : training_accuracy (float)
#-----------------------------------------------------------------------------------------------------
def calculate_training_accuracy(X_train, Y_train, trained_model):
    print(Border)
    print("Calculating Training Accuracy")
    print(Border)

    train_pred = trained_model.predict(X_train)
    training_accuracy = accuracy_score(Y_train, train_pred)
    print(f"Training Accuracy: {training_accuracy*100:.2f}%")
    return training_accuracy

#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_testing_accuracy
# Description      : Calculates and prints testing accuracy for the trained model
# Input            : Y_test (Series), predictions (array)
# Output           : testing_accuracy (float)
#-----------------------------------------------------------------------------------------------------
def calculate_testing_accuracy(Y_test, predictions):
    print(Border)
    print("Calculating Testing Accuracy")
    print(Border)

    testing_accuracy = accuracy_score(Y_test, predictions)
    print(f"Testing Accuracy: {testing_accuracy*100:.2f}%")
    return testing_accuracy

#-----------------------------------------------------------------------------------------------------
# Function Name    : display_confusion_matrix
# Description      : Displays confusion matrix for the testing set
# Input            : Y_test (Series), predictions (array)
# Output           : None (plots confusion matrix)
#-----------------------------------------------------------------------------------------------------
def display_confusion_matrix(Y_test, predictions):
    print(Border)
    print("Displaying Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test, predictions)
    print("Confusion Matrix:\n", cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title("Confusion Matrix of Student Performance")
    plt.show()

#-----------------------------------------------------------------------------------------------------
# Function Name    : test_model
# Description      : Predicts FinalResult for a custom input using the trained model
# Input            : trained_model (sklearn classifier)
# Output           : None (prints prediction)
#-----------------------------------------------------------------------------------------------------
def test_model(trained_model):
    print(Border)
    print("Testing Model with Custom Input")
    print(Border)

    custom_df = pd.DataFrame(
        [[6, 85, 66, 7, 7]],
        columns=["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    )

    result = trained_model.predict(custom_df)
    if result[0] == 1:
        print("Prediction: Student is likely to PASS")
    else:
        print("Prediction: Student is likely to FAIL")

#-----------------------------------------------------------------------------------------------------
# Function Name    : train_model
# Description      : Trains the Decision Tree model using the training dataset
# Input            : X_train (DataFrame), Y_train (Series), model (sklearn classifier)
# Output           : trained_model (sklearn classifier)
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
# Description      : Creates a Decision Tree classifier
# Input            : None
# Output           : model (DecisionTreeClassifier instance)
#-----------------------------------------------------------------------------------------------------
def build_model():
    print(Border)
    print("Building the Model")
    print(Border)

    model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
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
    print("Splitting Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("Y_train:", Y_train.shape)
    print("Y_test :", Y_test.shape)
    return X_train, X_test, Y_train, Y_test

#-----------------------------------------------------------------------------------------------------
# Function Name    : visualize_dataset
# Description      : Displays pairplot of dataset for exploratory data analysis
# Input            : df (DataFrame)
# Output           : None (plots visualization)
#-----------------------------------------------------------------------------------------------------
def visualize_dataset(df):
    print(Border)
    print("Visualizing Dataset")
    print(Border)
    sns.pairplot(df, hue="FinalResult")
    plt.show()

#-----------------------------------------------------------------------------------------------------
# Function Name    : analyze_data
# Description      : Prints dataset info and selects independent (features) and dependent (target) variables
# Input            : df (DataFrame)
# Output           : X (DataFrame), Y (Series)
#-----------------------------------------------------------------------------------------------------
def analyze_data(df):
    print(Border)
    print("Data Analysis and Feature Selection")
    print(Border)

    print("Shape of Dataset:", df.shape)
    print("Column Names:", list(df.columns))
    print("Missing Values per Column:\n", df.isnull().sum())
    print("Statistical Summary:\n", df.describe())

    feature_cols = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
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
# Description      : Driver function executing complete workflow: load, analyze, visualize, split, train, test, accuracy, confusion
#-----------------------------------------------------------------------------------------------------
def main():
    df = load_data()
    X, Y = analyze_data(df)
    visualize_dataset(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    model = build_model()
    trained_model = train_model(X_train, Y_train, model)
    predictions = trained_model.predict(X_test)
    test_model(trained_model)
    training_accuracy = calculate_training_accuracy(X_train, Y_train, trained_model)
    testing_accuracy = calculate_testing_accuracy(Y_test, predictions)
    display_confusion_matrix(Y_test, predictions)

#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()