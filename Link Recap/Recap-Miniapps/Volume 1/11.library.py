class Book:
    def __init__(self, author, title):
        self.author=author
        self.title=title
        
    def __str__(self):
        return f"The book {self.title} was written by {self.author}"
    
book1=Book("Paulo Coelho", "the Alchemyst")
print(book1)