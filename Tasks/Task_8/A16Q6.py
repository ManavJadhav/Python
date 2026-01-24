##################################################################################
#  Function name :     ChkNumType
#  Input :             int 
#  Output :            None
#  Description :       It used to check the number is positive, negative or zero.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
##################################################################################

def ChkNumType(No):
    
    if(No == 0):
        print("Zero")
    elif(No > 0):
        print("Positive Number")
    else:
        print("Negative Number")


def main():
    Value = 0

    print("Enter a number: ")
    Value = int(input())

    ChkNumType(Value)

if __name__ == "__main__":
    main()