###########################################################################
#  Function name :     Calculatelen
#  Input :             str 
#  Output :            int
#  Description :       It used to find length of a string.
#  Author :            Manav Mahadev Jadhav
#  Date :              22/01/2026
#
###########################################################################

def Calculatelen(strx):
   return len(strx)
        

def main():

    Ret = 0

    print("Enter a name : ")
    name = input()
    
    Ret = Calculatelen(name)
    print(Ret)

if __name__ == "__main__":
    main()