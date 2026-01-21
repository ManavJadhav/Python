###########################################################################
#  Function name :     BinaryEqui
#  Input :             int 
#  Output :            None
#  Description :       It used to find binary equivalent of a number.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def BinaryEqui(No):
    Result = ""
    if (No ==0 ):
        print(0)
    while(No != 0):
        BinRet = str (No % 2)
        Result = BinRet + Result
        No = No // 2
        
    print(Result)
    

def main():
    Value = 0

    print("Enter a number : ")
    Value = int(input())

    BinaryEqui(Value)
    

if __name__ == "__main__":
    main()