# Accept : Multiple Paramters
# Return : One value
def FunctionReturnDemo(Value1 , Value2):
    print("Inside FunctionReturnDemo :", Value1,Value2)
    return 11

def main():
    Result = None
    Result = FunctionReturnDemo("Python",21)
    print("Return Value is : ", Result)

if __name__ == "__main__":
    main()