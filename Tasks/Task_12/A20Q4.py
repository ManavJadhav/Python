######################################################################################################
# Program Name     : CountCharactersThreaded
# Input            : String from user
# Output           : Three integers
# Description      : Counts the number of lowercase letters, uppercase letters,
#                   and digit characters in a string using three separate threads.
# Author           : Manav Mahadev Jadhav
# Date             : 24/01/2026
######################################################################################################

import threading

#lobj = threading.Lock()

def CountSmall(chrx):
   print("Thread Name : ",threading.current_thread().name,"& Its ID :", threading.get_ident())
   
   iCnt = 0
   for i in range(len(chrx)):
    if(( chrx[i] >= 'a') and (chrx[i] <= 'z')):
       # with lobj :
       iCnt += 1
    
   print("Total number of lowercase characters are : ",iCnt)
  
def CountCapital(chrx):
    print("Thread Name : ",threading.current_thread().name,"& Its ID :", threading.get_ident())

    iCnt = 0
    for i in range(len(chrx)):
     if(( chrx[i] >= 'A') and (chrx[i] <= 'Z')):
       # with lobj :
       iCnt += 1
    
    print("Total number of uppercase characters are : ",iCnt)

def CountDigits(chrx):
    print("Thread Name : ",threading.current_thread().name,"& Its ID :", threading.get_ident())
    
    iCnt = 0
    for i in range(len(chrx)):
     if(( chrx[i] >= '0') and (chrx[i] <= '9')):
       # with lobj :
       iCnt += 1
    
    print("Total number of digits characters are : ",iCnt)

def main():

    print("Enter the string : ")
    Strx  = input()


    Small = threading.Thread(target=CountSmall, args=(Strx,), name="Small")
    Capital = threading.Thread(target=CountCapital, args=(Strx,), name="Capital")
    Digits = threading.Thread(target=CountDigits, args=(Strx,), name="Digits")


    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from :",threading.current_thread().name)

if __name__ == "__main__":
    main()