######################################################################################################
# Program Name     : BookStoreDemo
# Input            : Book name and author
# Output           : Prints book details and total number of books
# Description      : Demonstrates object-oriented programming using class variables
#                   to track the total number of BookStore objects created.
# Author           : Manav Mahadev Jadhav
# Date             : 27/01/2026
######################################################################################################

class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        self.Name = A
        self.Author =  B
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books :",BookStore.NoOfBooks)
    
    
def main():

    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()