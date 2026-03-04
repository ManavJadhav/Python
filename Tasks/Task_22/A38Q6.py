#=====================================================================================================
# Program Name     : StudentPerformanceStudyHoursHistogram
# Description      : Loads student performance dataset and visualizes the distribution of StudyHours
#                    using a histogram.
# Input            : student_performance_ml.csv
# Output           : Histogram showing distribution of StudyHours
# Author           : Manav Mahadev Jadhav
# Date             : 25/02/2026
# Dependencies     : pandas, matplotlib, seaborn
#=====================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------------------------------------------------------------------------------------------------
# Function Name    : plot_studyhours_histogram
# Description      : Generates a histogram to visualize the distribution of StudyHours.
# Input            : df (pandas DataFrame)
# Output           : Displays histogram of StudyHours
#-----------------------------------------------------------------------------------------------------
def plot_studyhours_histogram(df):
    Border = "-" * 40

    print(Border)
    print("Plotting Histogram of StudyHours")
    plt.figure(figsize=(10, 6))
    
    sns.histplot(
        data=df,
        x="StudyHours"
    )
    
    plt.title("Analysing StudyHours")
    plt.show()

    # Example observation (from dataset):
    # 1.0 - 2.3 Hours -> 6 students
    # 2.3 - 3.5 Hours -> 3 students
    # 3.5 - 4.7 Hours -> 5 students
    # 4.7 - 6.0 Hours -> 5 students
    # 6.0 - 7.2 Hours -> 6 students
    # 7.2 - 8.5 Hours -> 5 students

#-----------------------------------------------------------------------------------------------------
# Function Name    : Load_Data
# Description      : Loads the student performance dataset from CSV file and calls histogram plotting.
# Input            : None
# Output           : Displays histogram for StudyHours
#-----------------------------------------------------------------------------------------------------
def Load_Data():
    Dataset_Name = "student_performance_ml.csv"
    dataframe = pd.read_csv(Dataset_Name)
    plot_studyhours_histogram(dataframe)

#-----------------------------------------------------------------------------------------------------
# Function Name    : main
# Description      : Entry point of the program.
#                    Initiates data loading and histogram plotting workflow.
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