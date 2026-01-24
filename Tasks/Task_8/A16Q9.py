###########################################################################
#  Function name :     Display
#  Input :             None 
#  Output :            None
#  Description :       It used to display first 10 even numbers on screen.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def DisplayEven():
    iCnt = 0
    
    for i in range(1,50):
        if(iCnt < 10):
            if(i % 2 == 0):
                iCnt += 1
                print(i,end="\t")
    
    print()
        

def main():
    
    DisplayEven()

if __name__ == "__main__":
    main()