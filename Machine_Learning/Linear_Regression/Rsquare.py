from sklearn.metrics import r2_score


def main():
    Y_Actual = [3,4,2,4,5]      # Y
    Y_Predicted = [2.8,3.2,3.6,4.0,4.4] # Yp

    r2 = r2_score(Y_Actual,Y_Predicted)

    print("Actual values : Y ",Y_Actual)
    print("Predicted values : Yp ",Y_Predicted)

    print("R Sqaure value : ",r2)       # 0.307

if __name__ == "__main__":
    main()