from sklearn.metrics import r2_score


def main():
    Y_Actual = [3,4,2,4,5]      # Y
    Y_Predicted = [3,4,2,4,5] # Yp

    r2 = r2_score(Y_Actual,Y_Predicted)

    print("Actual values : Y ",Y_Actual)
    print("Predicted values : Yp ",Y_Predicted)

    print("R Sqaure value : ",r2)       # 1.0

if __name__ == "__main__":
    main()