import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def WineClassifier(DataPath):
    Border = "-" * 40

    # Step 1 : Load the dataset from CSV file
    print(Border)
    print("Step 1 : Load the dataset from CSV file")
    print(Border)
    

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from dataset : ")
    print(df.head())
    print(Border)


    # Step 2 : Clean the dataset by removing empty rows
    print(Border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)

    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])


    # Step 3 : Seperate Independent and Dependent variables
    print(Border)
    print("Step 3 : Seperate Independent and Dependent variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input Columns: ",X.columns.tolist())
    print("Output Columns : Class")
    print(Border)

def main():
    Border = "-" * 40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    WineClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()