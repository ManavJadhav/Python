class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

Obj = Demo()

print("End of Application")