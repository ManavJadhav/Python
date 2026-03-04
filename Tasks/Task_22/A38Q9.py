#=====================================================================================================
# Program Name     : StudentPerformanceAssignmentsBarPlot
# Description      : Loads student performance dataset and visualizes the relationship between
#                    AssignmentsCompleted and FinalResult using a bar plot.
# Input            : student_performance_ml.csv
# Output           : Bar plot showing AssignmentsCompleted vs FinalResult
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------------------------------------------
# Function Name    : plot_assignments_vs_result
# Description      : Generates a bar plot to visualize the relationship between
#                    AssignmentsCompleted and FinalResult.
# Input            : df (pandas DataFrame)
# Output           : Displays bar plot
#-----------------------------------------------------------------------------------------------------
def plot_assignments_vs_result(df):
    Border = "-" * 40

    print(Border)
    print("Plotting Relationship between AssignmentsCompleted and FinalResult")
    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=df,
        x="AssignmentsCompleted",
        y="FinalResult",
        errorbar=None
    )

    plt.title("Relationship between AssignmentsCompleted and FinalResult")
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")
    # Optional grid for better readability:
    # plt.grid(True, linestyle="--", alpha=0.5)

    plt.show()

    # Observation:
    # Students completing more than 5 assignments have a higher probability of passing.
    # Students completing exactly 5 assignments may pass or fail depending on other factors.

#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls the bar plot function.
# Input            : None
# Output           : Displays AssignmentsCompleted vs FinalResult bar plot
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    plot_assignments_vs_result(dataframe)

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and AssignmentsCompleted vs FinalResult bar plot workflow.
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