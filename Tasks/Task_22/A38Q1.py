#=====================================================================================================
# Program Name     : StudentPerformanceEDA
# Description      : Loads student performance dataset and provides basic exploratory data analysis
#                    including dataset preview, shape, column names, and data types.
# Input            : student_performance_ml.csv
# Output           : Prints first/last records, shape, column names, and data types
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas
#=====================================================================================================

import pandas as pd

#-----------------------------------------------------------------------------------------------------
# Function Name    : Display
# Description      : Displays a comprehensive overview of the dataframe including:
#                    - First 5 records
#                    - Last 5 records
#                    - Total number of rows and columns
#                    - List of column names
#                    - Data types of each column
# Input            : df (pandas DataFrame)
# Output           : Prints dataset overview to console
#-----------------------------------------------------------------------------------------------------
def Display(df):
    Border = "-"*90

    print(Border)
    print("First 5 records from the dataset is :")
    print(Border)
    print(df.head())

    print(Border)
    print("Last 5 records from the dataset is :")
    print(Border)
    print(df.tail())

    print(Border)
    print("Total number of rows and columns are :")
    print(Border)
    print(df.shape)

    print(Border)
    print("List of column names are : ")
    print(Border)
    print(list(df.columns))

    print(Border)
    print("Data type of each column is : ")
    print(Border)
    print(df.dtypes)


#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls Display()
# Input            : None
# Output           : Displays dataframe overview via Display()
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    Display(dataframe)


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and display workflow.
# Input            : None
# Output           : Executes complete EDA workflow
#-----------------------------------------------------------------------------------------------------
def main():
    Load_Data()


#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ =="__main__":
    main()