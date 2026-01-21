###########################################################################
#  Function name :     ChkVowel
#  Input :             Str 
#  Output :            bool
#  Description :       It used to check if a chacracter is a vowel or consonant.
#  Author :            Manav Mahadev Jadhav
#  Date :              20/01/2026
#
###########################################################################

def ChkVowel(char):
    flag = False

    if((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u') or (char == 'A') or (char == 'E') or (char == 'I') or (char == 'O') or (char == 'U')):
        flag = True
    return flag

def main():
    bRet = False

    print("Enter a charcter : ")
    strx = input()

    bRet = ChkVowel(strx)
    if(bRet == True):
        print("It is a Vowel")
    else:
        print("It is not a Vowel")


if __name__ == "__main__":
    main()