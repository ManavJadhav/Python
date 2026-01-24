###########################################################################
#  Function name :     Display
#  Input :             None 
#  Output :            None
#  Description :       It used to display * on screen.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def Display(No):
    for i in range(No):
        print("*",end="\t")
    print()

def main():
    Value = 0

    print("Enter a number: ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()