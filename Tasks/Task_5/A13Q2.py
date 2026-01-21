###########################################################################
#  Function name :     CircleArea
#  Input :             int  
#  Output :            int
#  Description :       It used to find Area of a Circle.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def CircleArea(radiusx):
    Area = 0
    PI = 3.14

    Area = PI * radiusx * radiusx

#   Area = PI * radiusx ** 2

    return Area

def main():

    No = 0
    Ret = 0

    print("Enter the radius of circle : ")
    No = int(input())

    Ret = CircleArea(No)
    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()