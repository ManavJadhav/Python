###########################################################################
#  Function name :     Display
#  Input :             int 
#  Output :            None
#  Description :       It used to display pattern on screen.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def Display(No):
    for i in range(1,No+1):
        print()
        for j in range(1,No+1):
                if(i >= j):
                    print(j, end="\t")

    print()

def main():
    Value = 0

    print("Enter a number: ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()