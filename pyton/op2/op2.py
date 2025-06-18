class Library:
    def __init__(self,list_of_bookes,name):
        self.bookList = list_of_bookes
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library {self.name}:")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.bookList:
            print("sorry,we do not have that book.")
        elif book in self.lendDict:
            print(f"sorry, is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print("Lender-Book database has been updated. You can take thr book now.")

    def addBook(self,book):
        self.bookList.append(book)
        print(f"{book} has been added to the book list.")

    def returnBook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("That book wasn't borrowed from us.")

if __name__ == '__main__':
        books = Library(['Python','Rich Dad Poor Dad','C++ Basics','Algorithms by CLRS'],"Let's upskill"
        )