###########################################################################
#  Function name :     DisplayMarks
#  Input :             int 
#  Output :            None
#  Description :       It used to display the gardes according to the marks. 
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def DisplayMarks(No):
    
    if((No >= 75)):
        print("Distinction")
    elif((No>=60)):
        print("First Class")
    elif((No>=50)):
        print("Second Class")
    else:
        print("Fail")
    
    

def main():
    Value = 0

    print("Enter the marks : ")
    Value = int(input())

    DisplayMarks(Value)
    

if __name__ == "__main__":
    main()