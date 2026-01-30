# Accept : Multiple Paramters
# Return : Multiple values
def FunctionReturnDemo(Value1 , Value2):
    print("Inside FunctionReturnDemo :", Value1,Value2)
    return 11,21 ,51

def main():
    Result1 = None
    Result2 = None
    Result3 = None

    Result1, Result2 ,Result3 = FunctionReturnDemo("Python",21)
    print("Return Value are : ", Result1, Result2, Result3)

if __name__ == "__main__":
    main()