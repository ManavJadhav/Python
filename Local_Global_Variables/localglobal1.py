No =11      # Global

def fun():
    No = 21 # Local
    print("Value of No from fun is: ", No)  # 21

print("value of No is: ",No)        # 11
fun()