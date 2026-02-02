No =11      # Global

def fun():
    No = 21
    print("Value of No from fun is: ", No)  # 21
    No = No + 1
    print("Value of No from fun is: ", No)  # 22

print("value of No is: ",No)        # 11
fun()
print("value of No is: ",No)