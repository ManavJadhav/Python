###########################################################################
#  Function name :     Display
#  Input :             None 
#  Output :            None
#  Description :       It used to display numbers from 1 to 10 in reverse order .
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def Display():
    for i in range(10,0,-1):
        print(i ,end="\t")
    print()

def main():

    Display()

if __name__ == "__main__":
    main()