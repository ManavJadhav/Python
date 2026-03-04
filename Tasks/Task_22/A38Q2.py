#=====================================================================================================
# Program Name     : StudentPerformancePassFailAnalysis
# Description      : Loads student performance dataset and provides counts of total students,
#                    number of students passed, and number of students failed.
# Input            : student_performance_ml.csv
# Output           : Prints total students, pass count, and fail count
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas
#=====================================================================================================

import pandas as pd

#-----------------------------------------------------------------------------------------------------
# Function Name    : Display
# Description      : Displays total number of students and counts of students who passed and failed.
# Input            : df (pandas DataFrame)
# Output           : Prints total students, pass count, and fail count
#-----------------------------------------------------------------------------------------------------
def Display(df):
    Border = "-"*40

    print(Border) 
    print("Total no. of students are : ", len(df))
    print(Border)

    print("No. of students Passed : ", df["FinalResult"].value_counts().get(1))
    print(Border)

    print("No. of students Failed : ", df["FinalResult"].value_counts().get(0))
    print(Border)


#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls Display().
# Input            : None
# Output           : Displays student pass/fail summary
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    Display(dataframe)


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and pass/fail summary display.
# Input            : None
# Output           : Executes complete workflow
#-----------------------------------------------------------------------------------------------------
def main():
    Load_Data()


#-----------------------------------------------------------------------------------------------------
# Program Execution Starts Here
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()