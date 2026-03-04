#=====================================================================================================
# Program Name     : StudentPerformancePassFailPercentage
# Description      : Loads student performance dataset and calculates distribution of FinalResult
#                    and percentage of students who passed and failed.
# Input            : student_performance_ml.csv
# Output           : Prints distribution and pass/fail percentages
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas
#=====================================================================================================

import pandas as pd

#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_percentage
# Description      : Computes and prints the distribution of FinalResult and the percentage of
#                    students who passed and failed.
# Input            : df (pandas DataFrame)
# Output           : Prints distribution and percentages to console
#-----------------------------------------------------------------------------------------------------
def calculate_percentage(df):
    Border = "-" * 40

    print(Border)
    FinalResult_dist = df["FinalResult"].value_counts()
    print("Distribution of FinalResult : ")
    print(Border)
    print(FinalResult_dist)

    print(Border)
    passed = FinalResult_dist.get(1)
    passed_percent = passed / len(df) * 100
    print(f"Percentage of students Passed : {passed_percent} %")
    print(Border)

    failed = FinalResult_dist.get(0)
    failed_percent = failed / len(df) * 100
    print(f"Percentage of students Failed : {failed_percent} %")
    print(Border)

    # Dataset is not perfectly balanced: 60% passed, 40% failed


#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls percentage function.
# Input            : None
# Output           : Displays FinalResult distribution and pass/fail percentages
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    calculate_percentage(dataframe)


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and percentage calculation workflow.
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