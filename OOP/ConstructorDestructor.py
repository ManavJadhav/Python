import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate
Obj = Demo()

# Use

# Deallocate
del Obj

gc.collect()

print("End of Application")