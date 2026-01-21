###########################################################################
#  Function name :     Display
#  Input :             int 
#  Output :            None
#  Description :       It used to display the numbers from 1 till input value.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def Display(No):

    for i in range(1,No+1):
       print(i,end=" ")


def main():
    
    Value = 0

    print("Enter a number : ")
    Value = int(input())

    Display(Value)
    print()


if __name__ == "__main__":
    main()