class Book:
    def __init__(self, title, author, publisher, tomeCount, edition):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.tomeCount = tomeCount
        self.edition = edition

    def __str__(self):
        return f"{self.title} ({self.publisher}) by {self.author} in {self.tomeCount} tomes, edition: {self.edition}"

    def book(self):
        return self