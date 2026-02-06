import threading

iCnt = 0

def Update():
    global iCnt

    for _ in range(2000000):
        iCnt = iCnt + 1


def main():
    global iCnt

    Update()
    Update()

    print("vaule of Icnt is : ",iCnt)

if __name__ == "__main__":
    main()