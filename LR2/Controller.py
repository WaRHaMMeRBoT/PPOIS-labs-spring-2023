from xml.dom import minidom
from Model import Book
from View import BookTableView
import xml.sax

class BookController:
    def __init__(self):
        self.books = []

    def addBook(self, title, author, publisher, tomeCount, edition):
        book = Book(title, author, publisher, tomeCount, edition)
        self.books.append(book)

    def deleteBook(self, book):
        self.books.remove(book)
    
    def saveFile(self, filename):
        doc = minidom.Document()
        root = doc.createElement('books')
        doc.appendChild(root)
        for book in self.books:
            bookElement = doc.createElement('book')
            root.appendChild(bookElement)

            titleElement = doc.createElement('title')
            titleElement.appendChild(doc.createTextNode(book.title))
            bookElement.appendChild(titleElement)

            authorElement = doc.createElement('author')
            authorElement.appendChild(doc.createTextNode(book.author))
            bookElement.appendChild(authorElement)

            publisherElement = doc.createElement('publisher')
            publisherElement.appendChild(doc.createTextNode(book.publisher))
            bookElement.appendChild(publisherElement)

            tomeCountElement = doc.createElement('tomeCount')
            tomeCountElement.appendChild(doc.createTextNode(str(book.tomeCount)))
            bookElement.appendChild(tomeCountElement)

            editionElement = doc.createElement('edition')
            editionElement.appendChild(doc.createTextNode(str(book.edition)))
            bookElement.appendChild(editionElement)
            
        with open(filename, 'w') as f:
            f.write(doc.toprettyxml())

    def loadFile(self, filename):
        try:
            handler = BookHandler()
            xml.sax.parse(filename, handler)
            self.books = handler.books
        except Exception as e:
            BookTableView.showErrorPopup()


class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.books = []
        self.currentData = ""
        self.title = ""
        self.author = ""
        self.publisher = ""
        self.tomeCount = ""
        self.edition = ""

    def startElement(self, tag, attributes):
        self.currentData = tag
        if tag == "book":
            self.title = ""
            self.author = ""
            self.publisher = ""
            self.tomeCount = ""
            self.edition = ""

    def endElement(self, tag):
        if tag == "book":
            book = Book(self.title, self.author, self.publisher, int(self.tomeCount), int(self.edition))
            self.books.append(book)
        self.currentData = None

    def characters(self, content):
        if self.currentData == "title":
            self.title = content
        elif self.currentData == "author":
            self.author = content
        elif self.currentData == "publisher":
            self.publisher = content
        elif self.currentData == "tomeCount":
            self.tomeCount = content
        elif self.currentData == "edition":
            self.edition = content