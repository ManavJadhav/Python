#=====================================================================================================
# Program Name     : StudentPerformanceSleepHoursBarPlot
# Description      : Loads student performance dataset and visualizes the relationship between
#                    SleepHours and FinalResult using a bar plot.
# Input            : student_performance_ml.csv
# Output           : Bar plot showing SleepHours vs FinalResult
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------------------------------------------
# Function Name    : plot_sleephours_vs_result
# Description      : Generates a bar plot to visualize the relationship between SleepHours and FinalResult.
# Input            : df (pandas DataFrame)
# Output           : Displays bar plot
#-----------------------------------------------------------------------------------------------------
def plot_sleephours_vs_result(df):
    Border = "-" * 40

    print(Border)
    print("Plotting SleepHours VS FinalResult")
    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=df,
        x="SleepHours",
        y="FinalResult",
        errorbar=None
    )

    plt.title("SleepHours VS FinalResult")
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")
    plt.show()

    # Observation:
    # Students who sleep more than 6 hours have a higher probability of passing.
    # Proper sleep helps students concentrate and perform better in exams.

#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls the SleepHours bar plot function.
# Input            : None
# Output           : Displays SleepHours vs FinalResult bar plot
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    plot_sleephours_vs_result(dataframe)

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and SleepHours vs FinalResult bar plot workflow.
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