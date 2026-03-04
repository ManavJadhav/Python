#=====================================================================================================
# Program Name     : StudentPerformanceLineAnalysis
# Description      : Loads student performance dataset and visualizes the impact of StudyHours
#                    and Attendance on FinalResult using line plots.
# Input            : student_performance_ml.csv
# Output           : Line plots showing StudyHours vs FinalResult and Attendance vs FinalResult
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------------------------------------------
# Function Name    : plot_study_attendance_vs_result
# Description      : Generates line plots to visualize the impact of StudyHours and Attendance
#                    on FinalResult.
# Input            : df (pandas DataFrame)
# Output           : Displays line plots for StudyHours vs FinalResult and Attendance vs FinalResult
#-----------------------------------------------------------------------------------------------------
def plot_study_attendance_vs_result(df):
    Border = "-" * 40

    # StudyHours vs FinalResult
    print(Border)
    print("StudyHours VS FinalResult")
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df,
        x="StudyHours",
        y="FinalResult",
        marker='o'
    )
    plt.title("Impact of Studying Hours on FinalResult")
    plt.xlabel("Number of Hours Studying")
    plt.ylabel("FinalResult")
    plt.show()
    
    # Attendance vs FinalResult
    print(Border)
    print("Attendance VS FinalResult")
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=df,
        x="Attendance",
        y="FinalResult",
        marker='o'
    )
    plt.title("Impact of Attendance on FinalResult")
    plt.xlabel("Attendance")
    plt.ylabel("FinalResult")
    plt.show()

    # Note: Higher StudyHours or Attendance correlates with higher probability of passing

#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls plotting function.
# Input            : None
# Output           : Displays line plots for StudyHours and Attendance vs FinalResult
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    plot_study_attendance_vs_result(dataframe)

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and visualization workflow.
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