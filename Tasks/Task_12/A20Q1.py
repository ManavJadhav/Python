######################################################################################################
# Function Name     : DisplayEven , DisplayOdd
#  Input            : None
#  Output           : None
#  Description      : Prints first 10 even and odd numbers using two threads.
#  Author           : Manav Mahadev Jadhav
#  Date             : 24/01/2026
######################################################################################################
import threading

#lobj = threading.Lock()

def DisplayEven():
    # with lobj :
    print("Inside : ",threading.current_thread().name)
    
    for i in range(2, 21, 2):
        print(i)

def DisplayOdd():
    # with lobj:
    print("Inside : ",threading.current_thread().name)

    for i in range(1, 20, 2):
        print(i)


def main():
    print("Inside : ",threading.current_thread().name)

    Even = threading.Thread(target=DisplayEven)
    Even.start()

    Odd = threading.Thread(target=DisplayOdd)
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()