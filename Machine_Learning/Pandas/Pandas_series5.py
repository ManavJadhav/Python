import pandas as pd

def main():

    sobj = pd.Series([25000,27000,29000,30000],index =["A","B","C","D"])

    print(sobj)

    print(sobj["C"])

if __name__ =="__main__":
    main()