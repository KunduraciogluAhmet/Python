from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

fontTitle = QFont("Arial", 26)
fontText = QFont("Arial", 16)

class Help(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Us")
        self.setGeometry(200,200,400,200)
        self.UI()
    
    def UI(self):
        vbox = QVBoxLayout(self)
        textTitle = QLabel("About Us")
        textAboutus = QLabel("This APP inspired by Mr Volkan Atis course on Udemy\n"
                             "You can get info from UDEMY\n"
                             "Only coded for educational purposes\n"
                             "coded using Python and PyQt5")
        textTitle.setFont(fontTitle)
        textAboutus.setFont(fontText)
        vbox.addWidget(textTitle)
        vbox.addWidget(textAboutus)
        self.setLayout(vbox)
