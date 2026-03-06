#=====================================================================================================
# CaseStudy Name    : Student Performance Prediction using Decision Tree
# Description       : Builds a Decision Tree model, evaluates it, and predicts student performance
# Input             : student_performance_ml.csv
# Output            : Predicted Final Result for custom input, training/testing accuracy, confusion matrix
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
# Description      : Displays confusion matrix for the testing set.
# Input            : Y_test (Series), predicted results (array)
# Output           : None (plots confusion matrix)
#-----------------------------------------------------------------------------------------------------
def display_confusion_matrix(Y_test, Y_pred):
    print(Border)
    print("Displaying Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix:\n", cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title("Confusion Matrix of Student Performance")
    plt.show()


#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_accuracy
# Description      : Calculates and prints training and testing accuracy.
# Input            : trained_model, X_train, Y_train, X_test, Y_test
# Output           : training_accuracy, testing_accuracy
#-----------------------------------------------------------------------------------------------------
def calculate_accuracy(trained_model, X_train, Y_train, X_test, Y_test):
    print(Border)
    print("Calculating Training and Testing Accuracy")
    print(Border)

    train_pred = trained_model.predict(X_train)
    test_pred = trained_model.predict(X_test)

    training_accuracy = accuracy_score(Y_train, train_pred)
    testing_accuracy = accuracy_score(Y_test, test_pred)

    print(f"Training Accuracy: {training_accuracy*100:.2f}%")
    print(f"Testing Accuracy : {testing_accuracy*100:.2f}%")

    return training_accuracy, testing_accuracy


#-----------------------------------------------------------------------------------------------------
# Function Name    : test_model
# Description      : Predicts FinalResult for a custom input using the trained model.
# Input            : trained_model (sklearn classifier)
# Output           : None (prints prediction)
#-----------------------------------------------------------------------------------------------------
def test_model(trained_model):
    print(Border)
    print("Testing the Model with Custom Input")
    print(Border)

    custom_df = pd.DataFrame([[6, 85, 66, 7, 7]],
                             columns=["StudyHours", "Attendance", "PreviousScore",
                                      "AssignmentsCompleted", "SleepHours"])

    result = trained_model.predict(custom_df)
    if result[0] == 1:
        print("Prediction : Student is likely to PASS")
    else:
        print("Prediction : Student is likely to FAIL")


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

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

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

    feature_cols = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
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
# Description      : Driver function to execute complete workflow: load data, analyze, split, build/train model, test, accuracy, confusion.
#-----------------------------------------------------------------------------------------------------
def main():
    df = load_data()
    X, Y = analyze_data(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    model = build_model()
    trained_model = train_model(X_train, Y_train, model)
    test_model(trained_model)
    training_accuracy, testing_accuracy = calculate_accuracy(trained_model, X_train, Y_train, X_test, Y_test)
    display_confusion_matrix(Y_test, trained_model.predict(X_test))


#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()