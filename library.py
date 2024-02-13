class Library:
    def __init__(self):
        # open books.txt with a+ mode.
        self.file = open("books.txt", "a+")

    def __del__(self):
        # close books.txt
        self.file.close()

    def listBooks(self):
        """
        i. Read the contents of the file.
        ii. Add each line to a list using splitlines() method of the string object.
        iii. Now each element of the list holds information about a single book.
             Print book names and authors using this information.
        """
        self.file.seek(0)  # move to beginning
        #books = self.file.readlines()
        books = self.file.read().splitlines()
        print("your books;")
        for book in books:
            title, author, _, _ = book.strip().split(",")
            print(f"Title: {title}, Author: {author}")

    def addBook(self):
        """
        i. Ask user input for book title, book author, first release year and number
           of pages
        ii. Create a string with this information. Add book title then comma then
            author then comma etc.
        iii. Append this line to the file.
        """
        title = input("title of book: ")
        author = input("author of book: ")
        year = input("year of book: ")
        pages = input("pages of book: ")
        self.file.write(f"{title}, {author}, {year}, {pages}\n")
        print(f"{title} by {author} added to library")

    def removeBook(self):
        """
        i. Ask the user input for book title.
        ii. Read the file contents and add book to a list (just like you did while
            creating a list books method).
        iii. Find the index of the book to be deleted in the list.
        iv. Remove the book from the list.
        v. Remove the contents of the books.txt.
        vi. Add all elements of the list to the books.txt.

        * With this method you remove contents of the books.txt and rewrite
        the new list. If you don’t remove the contents, it will add the same
        books again to the file.
        """
        title = input("title of book: ")
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            if book.split(",")[0] == title:
                print(f"{book.split(",")[0]} by {book.split(",")[1]} removed from library")
                books.remove(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(books)

lib = Library()
while(True):
    choose = input("Menu\nadd|remove|list|exit\nyour choice => ")

    if choose in ["add","1"]:
        lib.addBook()
    elif choose in ["remove","2"]:
        lib.removeBook()
    elif choose in ["list","3"]:
        lib.listBooks()
    elif choose in ["exit","4"]:
        print("See you next time!")
        break
    else:
        print("Invalid choice")
    print("-------------\n")