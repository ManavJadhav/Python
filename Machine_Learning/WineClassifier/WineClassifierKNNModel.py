import pandas as pd
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

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


    # Step 3 : Separate Independent and Dependent variables
    print(Border)
    print("Step 3 : Separate Independent and Dependent variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input Columns: ",X.columns.tolist())
    print("Output Columns : Class")
    print(Border)

    # Step 4 : Split the dataset for training and testing
    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Information of training and testing data")
    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)
    print(Border)

    # Step 5 : Feature Scaling
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()
    
    # Independent Variable Scaling
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test) 

    print("Feature Scaling is done")

    # Step 6 : Explore multiple values of k
    # Hyperparameter tuning (k)

    print(Border)
    print("Step 6 : Explore multiple values of k")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)


def main():
    Border = "-" * 40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    WineClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()