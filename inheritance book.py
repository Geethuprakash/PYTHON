class Publisher:
    def __init__ (self, name):
        self.name=name
    def display(self):
        print(f"Publisher: {self.name}")

class Book(Publisher):
    def __init__(self, name, title, author, ):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")

class Python(Book):
    def __init__(self, name, title, author, price,page_no):
        super().__init__(name,title,author)
        self.price=price
        self.page_no=page_no
    def display(self):
        super().display()
        print(f"Book Price:{self.price}")
        print(f"Total Pages in Book:{self.page_no}")

first_book=(Python("Marvel","Wings of Fire","APJ Abdul Kalam",2000,150))
first_book.display()
second_book=(Book("DC Books","kerala vs Human","Pv narasimha rao"))
second_book.display()