from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserListView
from Controller import BookController
import math
import os

Builder.load_string('''
<BookView>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class GeneralFilterPopup(Popup):
    def __init__(self, books, callback, mode: str, **kwargs):
        super().__init__(title='Choose filter parameter', **kwargs)
        self.books = books
        self.callback = callback
        self.titleFilter_button = Button(text='Title', on_press=self.titleFilter_popup)
        self.authorFilter_button = Button(text='Author', on_press=self.authorFilter_popup)
        self.publisherAndAuthorFilter_button = Button(text='Publisher and author', on_press=self.publisherAndAuthorFilter_popup)
        self.tomeCountFilter_button = Button(text='Tome count', on_press=self.tomeCountFilter_popup)
        self.editionFilter_button = Button(text='Edition', on_press=self.editionFilter_popup)
        self.cancel_button = Button(text='Cancel', on_press=self.dismiss)
        self.filteredBooks = []
        self.mode = mode
        self.textInput1 = TextInput(text='')
        self.textInput2 = TextInput(text='')
        self.content = self.build_layout()

    def build_layout(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.titleFilter_button)
        layout.add_widget(self.authorFilter_button)
        layout.add_widget(self.publisherAndAuthorFilter_button)
        layout.add_widget(self.tomeCountFilter_button)
        layout.add_widget(self.editionFilter_button)
        layout.add_widget(self.cancel_button)
        return layout

    def titleFilter_popup(self, instance):
        newContent = BoxLayout(orientation='vertical')
        self.textInput1.hint_text = "Title"
        newContent.add_widget(self.textInput1)

        newContent.add_widget(Button(text = self.mode, on_press=self.titleFilter))
        dialog = Popup(title='Enter value', content=newContent, size_hint=(None, None), size=(400, 400))
        dialog.open()
        self.dismiss()

    def authorFilter_popup(self, instance):
        newContent = BoxLayout(orientation='vertical')
        self.textInput1.hint_text = "Author"
        newContent.add_widget(self.textInput1)

        newContent.add_widget(Button(text = self.mode, on_press=self.authorFilter))
        Popup(title='Enter value', content=newContent, size_hint=(None, None), size=(400, 400)).open()

    def publisherAndAuthorFilter_popup(self, instance):
        newContent = BoxLayout(orientation='vertical')
        self.textInput1.hint_text = "Publisher"
        self.textInput2.hint_text = "Author"
        newContent.add_widget(self.textInput1)
        newContent.add_widget(self.textInput2)

        newContent.add_widget(Button(text = self.mode, on_press=self.publisherAndAuthorFilter))
        Popup(title='Enter value', content=newContent, size_hint=(None, None), size=(400, 400)).open()

    def tomeCountFilter_popup(self, instance):
        newContent = BoxLayout(orientation='vertical')
        self.textInput1.hint_text = "From"
        self.textInput2.hint_text = "To"
        newContent.add_widget(self.textInput1)
        newContent.add_widget(self.textInput2)
        self.textInput1.input_filter = 'int'
        self.textInput2.input_filter = 'int'
        newContent.add_widget(Button(text = self.mode, on_press=self.tomeCountFilter))
        Popup(title='Enter value', content=newContent, size_hint=(None, None), size=(400, 400)).open()

    def editionFilter_popup(self, instance):
        newContent = BoxLayout(orientation='vertical')
        self.textInput1.hint_text = "From"
        self.textInput2.hint_text = "To"
        newContent.add_widget(self.textInput1)
        newContent.add_widget(self.textInput2)
        self.textInput1.input_filter = 'int'
        self.textInput2.input_filter = 'int'
        newContent.add_widget(Button(text = self.mode, on_press=self.editionFilter))
        Popup(title='Enter value', content=newContent, size_hint=(None, None), size=(400, 400)).open()

    def titleFilter(self, instance):
        self.filteredBooks = [book for book in self.books if self.textInput1.text.lower() in book.title.lower()]
        self.callback(self.filteredBooks, instance)

    def authorFilter(self, instance):
        self.filteredBooks = [book for book in self.books if self.textInput1.text.lower() in book.author.lower()]
        self.callback(self.filteredBooks, instance)

    def publisherAndAuthorFilter(self, instance):
        self.filteredBooks = [book for book in self.books if self.textInput1.text.lower() in book.publisher.lower() and self.textInput2.text.lower() in book.author.lower()]
        self.callback(self.filteredBooks, instance)

    def tomeCountFilter(self, instance):
        self.filteredBooks = [book for book in self.books if int(self.textInput1.text) <= int(book.tomeCount) and int(self.textInput2.text) >= int(book.tomeCount)]
        self.callback(self.filteredBooks, instance)

    def editionFilter(self, instance):
        self.filteredBooks = [book for book in self.books if int(self.textInput1.text) <= int(book.edition) and int(self.textInput2.text) >= int(book.edition)]
        self.callback(self.filteredBooks, instance)

class SaveLoadPopup(Popup):
    def __init__(self, fileType, callback, **kwargs):
        super().__init__(**kwargs)
        self.fileType = fileType
        self.callback = callback
        self.fileChooser = FileChooserListView(path=os.getcwd())
        self.saveButton = Button(text='Save' if fileType == 'save' else 'Load', on_press=self.handleSaveLoad)
        self.title = 'Save' if fileType == 'save' else 'Load'
        self.cancelButton = Button(text='Cancel', on_press=self.dismiss)
        self.content = self.buildLayout()

    def buildLayout(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.fileChooser)
        layout.add_widget(self.saveButton)
        layout.add_widget(self.cancelButton)
        return layout

    def handleSaveLoad(self, instance):
        if self.fileType == 'save':
            if len(self.fileChooser.selection) == 0:
                self.callback(os.path.join(os.getcwd(), "save"))
            else:
                selectedFile = self.fileChooser.selection[0]
                self.callback(selectedFile)
        elif self.fileType == 'load':
            if len(self.fileChooser.selection) != 0:
                selectedFile = self.fileChooser.selection[0]
                self.callback(selectedFile)
        
        BookTableView.tryFirstPage(instance)
        self.dismiss()

class BookView(RecycleView):
    def __init__(self, books, booksPerPage, **kwargs):
        super(BookView, self).__init__(**kwargs)
        self.currentPage = 0
        self.booksPerPage = booksPerPage
        self.update(books)

    def update(self, newData):
        endIndex = min(len(newData), self.currentPage * self.booksPerPage + self.booksPerPage)
        startIndex = max(0, self.currentPage * self.booksPerPage)
        self.data = [{'text':str(newData[i])} for i in range(startIndex, endIndex)]

    def showPreviousPage(self, books):
        if (self.currentPage > 0):
            self.currentPage -= 1
            self.update(books)

    def showNextPage(self, books):
        if (self.currentPage * self.booksPerPage + self.booksPerPage < len(books)):
            self.currentPage += 1
            self.update(books)

    def showFirstPage(self, books):
        self.currentPage = 0
        self.update(books)

    def showLastPage(self, books):
        if (len(books) > 0):
            self.currentPage = math.ceil(len(books) / self.booksPerPage) - 1
            self.update(books)


class BookTableView(App):
    bookController: BookController
    bookView: BookView
    pageInfo = Label()
    booksShown = Label()
    totalBooks = Label()
    def build(self):
        headLayout = BoxLayout(orientation="vertical")

        BookTableView.bookController = BookController()
        BookTableView.bookView = BookView(BookTableView.bookController.books, 10)
        addButton = Button(text = "Add", on_press=BookTableView.showAddPopup)

        searchButton = Button(text = "Search", on_press=BookTableView.showSearchPopup)
        deleteButton = Button(text = "Delete", on_press=BookTableView.showDeletePopup)

        saveButton = Button(text = "Save", on_press=BookTableView.showSavePopup)
        loadButton = Button(text = "Load", on_press=BookTableView.showLoadPopup)

        firstPageButton = Button(text = "|<", on_press= BookTableView.tryFirstPage)
        lastPageButton = Button(text = ">|", on_press= BookTableView.tryLastPage)
        nextPageButton = Button(text = ">", on_press= BookTableView.tryNextPage)
        previousPageButton = Button(text = "<", on_press= BookTableView.tryPreviousPage)

        buttons = BoxLayout(orientation="vertical")
        buttons.add_widget(addButton)
        buttons.add_widget(searchButton)
        buttons.add_widget(deleteButton)
        buttons.add_widget(lastPageButton)
        buttons.add_widget(nextPageButton)
        buttons.add_widget(previousPageButton)
        buttons.add_widget(firstPageButton)
        buttons.add_widget(saveButton)
        buttons.add_widget(loadButton)
        buttons.size_hint = (0.3, 1)

        mainContent = BoxLayout(orientation="horizontal")
        mainContent.add_widget(BookTableView.bookView)
        mainContent.add_widget(buttons)
        mainContent.size_hint = (0.7, 1)

        statsContent = BoxLayout(orientation="horizontal")
        BookTableView.updateLabels()
        statsContent.add_widget(BookTableView.pageInfo)
        statsContent.add_widget(BookTableView.booksShown)
        statsContent.add_widget(BookTableView.totalBooks)
        mainContent.size_hint = (1, 0.8)
        statsContent.size_hint = (1, 0.2)
        headLayout.add_widget(mainContent)
        headLayout.add_widget(statsContent) 
        return headLayout

    def showSearchPopup(instance):
        searchDialog = GeneralFilterPopup(BookTableView.bookController.books, BookTableView.searchAndShowResults, "Search")
        searchDialog.open()

    def searchAndShowResults(books, instance):
        BookTableView.showFilterResults(books, "Search results")

    def showDeletePopup(instance):
        deleteDialog = GeneralFilterPopup(BookTableView.bookController.books, BookTableView.deleteAndShowResults, "Delete")
        deleteDialog.open()

    def deleteAndShowResults(books, instance):
        BookTableView.showFilterResults(books, "Delete results")
        for book in books:
            BookTableView.bookController.deleteBook(book)
        BookTableView.tryFirstPage(instance)

    def showFilterResults(books, text):
        dialogContent = BoxLayout(orientation='vertical', spacing=10)
        foundBookView = BookView(books, 50)
        dialogContent.add_widget(foundBookView)
        Popup(title=text, content=dialogContent, size_hint=(None, None), size=(800, 400)).open()

    def showSavePopup(instance):
        save_dialog = SaveLoadPopup(fileType='save', callback=BookTableView.bookController.saveFile)
        save_dialog.open()

    def showLoadPopup(instance):
        load_dialog = SaveLoadPopup(fileType='load', callback=BookTableView.bookController.loadFile)
        load_dialog.open()
            
    def updateLabels():
        BookTableView.pageInfo.text = "Page: " + str(BookTableView.bookView.currentPage + 1) + " of " + str(math.ceil(len(BookTableView.bookController.books) / 10))
        BookTableView.booksShown.text = "Books on current page: " + str(len(BookTableView.bookView.data))
        BookTableView.totalBooks.text = "Total books: " + str(len(BookTableView.bookController.books))

    def tryFirstPage(instance):
        if (BookTableView.bookController.books != None):
            BookTableView.bookView.showFirstPage(BookTableView.bookController.books)
        BookTableView.updateLabels()

    def tryNextPage(instance):
        if (BookTableView.bookController.books != None):
            BookTableView.bookView.showNextPage(BookTableView.bookController.books)
        BookTableView.updateLabels()

    def tryLastPage(instance):
        if (BookTableView.bookController.books != None):
            BookTableView.bookView.showLastPage(BookTableView.bookController.books)
        BookTableView.updateLabels()

    def tryPreviousPage(instance):
        if (BookTableView.bookController.books != None):
            BookTableView.bookView.showPreviousPage(BookTableView.bookController.books)
        BookTableView.updateLabels()

    def showErrorPopup():
        popup_content = Label(text='Error')
        popup = Popup(title='Error', content=popup_content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def showAddPopup(instance):
        dialog = AddPopup(BookTableView.addBook)
        dialog.open()
            
    def addBook(title, author, publisher, tomeCount, edition, instance):
        BookTableView.bookController.addBook(title, author, publisher, tomeCount, edition)
        BookTableView.tryFirstPage(instance)

class AddPopup(Popup):
    def __init__(self, callback, **kwargs):
        super().__init__(title='Add Book', **kwargs)
        self.callback = callback
        self.titleInput = TextInput(text='', hint_text='Title')
        self.authorInput = TextInput(text='', hint_text='Author')
        self.publisherInput = TextInput(text='', hint_text='Publisher')
        self.tomeCountInput = TextInput(text='', hint_text='Tomes')
        self.editionInput = TextInput(text='', hint_text='Edition')
        self.tomeCountInput.input_filter = 'int'
        self.editionInput.input_filter = 'int'
        self.ok_button = Button(text='Add')
        self.cancel_button = Button(text='Cancel')
        self.ok_button.bind(on_press=self.tryReturnInput)
        self.cancel_button.bind(on_press=self.dismiss)
        self.content = self.build_layout()

    def build_layout(self):
        dialogContent = BoxLayout(orientation='vertical', spacing=10)
        dialogContent.add_widget(self.titleInput)
        dialogContent.add_widget(self.authorInput)
        dialogContent.add_widget(self.publisherInput)
        dialogContent.add_widget(self.tomeCountInput)
        dialogContent.add_widget(self.editionInput)
        
        button_box = BoxLayout(orientation='horizontal')
        button_box.add_widget(self.ok_button)
        button_box.add_widget(self.cancel_button)

        dialogContent.add_widget(button_box)
        return dialogContent

    def tryReturnInput(self, instance):
        try:
            title = self.titleInput.text
            author = self.authorInput.text
            publisher = self.publisherInput.text
            tomeCount = int(self.tomeCountInput.text)
            edition = int(self.editionInput.text)
            self.callback(title, author, publisher, tomeCount, edition, instance)
        except Exception as E:
            BookTableView.showErrorPopup()
        self.dismiss() 