from sklearn.datasets import load_iris


def main():
    print("Iris Classsification case study")

    Dataset = load_iris()
    
    # Metadata of Dataset
    print("Independent variable are : ")
    print(Dataset.feature_names)

    print("Dependent variables are : ")
    print(Dataset.target_names)


if __name__ =="__main__":
    main()

