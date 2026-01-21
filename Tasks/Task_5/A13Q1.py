###########################################################################
#  Function name :     RectArea
#  Input :             int , int 
#  Output :            int
#  Description :       It used to find Area of a Rectangle.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def RectArea(lengthx,widthx):
    Area = 0

    Area = lengthx * widthx

    return Area

def main():
    No1 = 0
    No2 = 0
    Ret = 0

    print("Enter the length of rectangle : ")
    No1 = int(input())

    print("Enter the width of rectangle : ")
    No2 = int(input())

    Ret = RectArea(No1,No2)
    print("Area of Rectangle is : ",Ret)

if __name__ == "__main__":
    main()