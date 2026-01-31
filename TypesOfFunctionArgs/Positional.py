def Display(A,B,C,D):
    print(A,B,C,D)

def main():
   # Display(10,20)                 NOT ALLOWED -> Less Arguments
   # Display(10,20,30,40,50)        NOT ALLOWED -> Extra Arguments
   Display(10,20,30,40)            #ALLOWED 


if __name__ == "__main__":
    main()