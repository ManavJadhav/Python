#=====================================================================================================
# Program Name     : StudentPerformanceStudyHoursPreviousScoreScatter
# Description      : Loads student performance dataset and visualizes StudyHours vs PreviousScore
#                    using a scatter plot colored by FinalResult (Pass/Fail).
# Input            : student_performance_ml.csv
# Output           : Scatter plot showing StudyHours vs PreviousScore with pass/fail coloring
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------------------------------------------
# Function Name    : plot_studyhours_previousscore_scatter
# Description      : Generates a scatter plot of StudyHours vs PreviousScore, with points
#                    colored by FinalResult (Pass/Fail).
# Input            : df (pandas DataFrame)
# Output           : Displays scatter plot
#-----------------------------------------------------------------------------------------------------
def plot_studyhours_previousscore_scatter(df):
    Border = "-" * 40

    print(Border)
    print("Plotting Scatter Plot of StudyHours VS PreviousScore")

    plt.figure(figsize=(10, 6))

    # Map 0/1 FinalResult to 'Fail'/'Pass' for legend clarity
    df['Result'] = df['FinalResult'].map({0: 'Fail', 1: 'Pass'})

    sns.scatterplot(
        data=df,
        x="StudyHours",
        y="PreviousScore",
        hue="Result",
        palette={'Fail': 'red', 'Pass': 'green'},
        s=100
    )

    plt.title("StudyHours VS PreviousScore")
    plt.show()

#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls scatter plot function.
# Input            : None
# Output           : Displays StudyHours vs PreviousScore scatter plot
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    plot_studyhours_previousscore_scatter(dataframe)

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and scatter plot workflow.
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