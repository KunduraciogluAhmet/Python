import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp, QSize
import time
import sqlite3
import main

con=sqlite3.connect("library.db")
cur= con.cursor()

class DisplayBook(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My Library")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(350,100,450,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
        
    def UI(self):
        ######### GETTING THE DETAILS OF BOOK ##############
        global book_id
        book=cur.execute("SELECT * FROM books WHERE book_id=?", (book_id,)).fetchall()
        print(book)
        self.setStyleSheet("background-color:white")
        main_layout=QVBoxLayout()
        topFrame= QFrame(self)
        topFrame.setStyleSheet("background-color:white")
        top_layout= QHBoxLayout(topFrame)
        bottomFrame=QFrame(self)
        bottom_layout=QFormLayout(bottomFrame)
        bottomFrame.setStyleSheet("font: 15pt Times Bold; background-color:#fcc324")


        img_book= QLabel(topFrame)
        img=QPixmap("icons/addbook.png")
        img_book.setPixmap(img)
        lbl_title= QLabel("Display Book", topFrame)
        lbl_title.setStyleSheet("color:#003f8a; font: 25pt Times Bold")
        top_layout.addStretch()
        top_layout.addWidget(img_book)
        top_layout.addWidget(lbl_title)
        top_layout.addStretch()
        main_layout.addWidget(topFrame)

        ##################### BOTTOM FRAME DESIGN ###############

        ################ ENTRIES ##############

        self.name_entry=QLineEdit(bottomFrame)
        self.name_entry.setPlaceholderText("Book's Name")
        self.name_entry.setStyleSheet("background-color:#fefeef")
        self.author_entry=QLineEdit(bottomFrame)
        self.author_entry.setPlaceholderText("Author's Name")
        self.author_entry.setStyleSheet("background-color:#fefeef")
        self.page_entry=QLineEdit(bottomFrame)
        self.page_entry.setPlaceholderText("Pages")
        self.page_entry.setStyleSheet("background-color:#fefeef")
        self.lang_entry=QLineEdit(bottomFrame)
        self.lang_entry.setPlaceholderText("Book's Language")
        self.lang_entry.setStyleSheet("background-color:#fefeef")
        self.description=QTextEdit(bottomFrame)
        self.description.setStyleSheet("background-color:#fefeef")

        add_button=QPushButton("Add", bottomFrame)
        add_button.setStyleSheet("background-color:#dadade")
        add_button.clicked.connect(self.addBook)

        bottom_layout.addRow(QLabel("Name :"),self.name_entry)
        bottom_layout.addRow(QLabel("Author :"),self.author_entry)
        bottom_layout.addRow(QLabel("Page :"),self.page_entry)
        bottom_layout.addRow(QLabel("Language :"),self.lang_entry)
        bottom_layout.addRow(QLabel("Description :"),self.description)
        bottom_layout.addRow(QLabel(""),add_button)
        main_layout.addWidget(bottomFrame)

        


        self.setLayout(main_layout)

    def addBook(self):
        name=self.name_entry.text()
        author=self.author_entry.text()
        page=self.page_entry.text()
        language=self.lang_entry.text()
        description=self.description.toPlainText()

        if name and author and page and language and description:
            try:
                query = "INSERT INTO books (book_name, book_author, book_page, book_language, book_details) VALUES (?, ?, ?, ?, ?)"
                cur.execute(query, (name, author, page, language, description))
                con.commit()
                QMessageBox.information(self, "Information", "New Book has been added to file")
                self.name_entry.setText("")
                self.author_entry.setText("")
                self.page_entry.setText("")
                self.lang_entry.setText("")
                self.description.setText("")
            except Exception as e:
                QMessageBox.information(self, "Warning", f"New Book couldn't be added: {str(e)}")
        else:
            QMessageBox.information(self, "Information", "Fields CANNOT be empty")

        """
        self.mainpage= main.Main()
        self.mainpage.tabs.update() 
        """