#=====================================================================================================
# Program Name     : StudentPerformanceAttendanceBoxplot
# Description      : Loads student performance dataset and visualizes Attendance using a boxplot
#                    to analyze outliers.
# Input            : student_performance_ml.csv
# Output           : Boxplot of Attendance
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------------------------------------------
# Function Name    : plot_attendance_boxplot
# Description      : Generates a boxplot to visualize Attendance and detect outliers.
# Input            : df (pandas DataFrame)
# Output           : Displays boxplot of Attendance
#-----------------------------------------------------------------------------------------------------
def plot_attendance_boxplot(df):
    Border = "-" * 40

    print(Border)
    print("Plotting Boxplot of Attendance")
    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="Attendance"
    )

    plt.title("Analysing Outliers in Attendance")
    plt.xlabel("Attendance (%)")
    plt.show()

#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls boxplot function.
# Input            : None
# Output           : Displays Attendance boxplot
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    plot_attendance_boxplot(dataframe)

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and Attendance boxplot workflow.
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