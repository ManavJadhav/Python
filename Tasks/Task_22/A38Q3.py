#=====================================================================================================
# Program Name     : StudentPerformanceStatistics
# Description      : Loads student performance dataset and calculates key statistics including
#                    average StudyHours, average Attendance, maximum PreviousScore, and minimum SleepHours.
# Input            : student_performance_ml.csv
# Output           : Prints calculated statistics
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas
#=====================================================================================================

import pandas as pd

#-----------------------------------------------------------------------------------------------------
# Function Name    : calculate_statistics
# Description      : Computes and prints the following statistics:
#                    - Average StudyHours
#                    - Average Attendance
#                    - Maximum PreviousScore
#                    - Minimum SleepHours
# Input            : df (pandas DataFrame)
# Output           : Prints statistics to console
#-----------------------------------------------------------------------------------------------------
def calculate_statistics(df):
    Border = "-"*40

    print(Border)
    print("Average of StudyHours : ", df["StudyHours"].mean())
    print(Border)

    print("Average of Attendance : ", df["Attendance"].mean())
    print(Border)

    print("Maximum of PreviousScore : ", df["PreviousScore"].max())
    print(Border)

    print("Minimum of SleepHours : ", df["SleepHours"].min())
    print(Border)


#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls statistics function.
# Input            : None
# Output           : Displays calculated statistics
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    calculate_statistics(dataframe)


#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and statistics calculation workflow.
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