import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRegExp, QSize
import time
import about
textChanged = False
url = ""
tbchecked = True
dockChecked= True
statusbarchecked=True


class FindDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Find&Replace")
        self.setGeometry(450, 200, 350, 250)
        self.UI()

    def UI(self):
        formLayout = QFormLayout(self)
        hbox = QHBoxLayout()
        txtFind = QLabel("Find   :")
        txtReplace = QLabel("Replace :")
        txtEmpty = QLabel("")
        self.findInput = QLineEdit()
        self.ReplaceInput = QLineEdit()
        self.btnFind = QPushButton("Find")
        self.btnReplace = QPushButton("Replace")
        hbox.addWidget(self.btnFind)
        hbox.addWidget(self.btnReplace)
        formLayout.addRow(txtFind, self.findInput)
        formLayout.addRow(txtReplace, self.ReplaceInput)
        formLayout.addRow(txtEmpty, hbox)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Text Editor")
        self.setWindowIcon(QIcon("icons/notepad.png"))
        self.setGeometry(50, 40, 1050, 800)
        self.UI()
    
    def UI(self):
        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(12.0)
        self.editor.textChanged.connect(self.funcTextChanged)
        self.menu()
        self.toolbar()
        self.dockbar()
        self.statusbar()

        self.show()
    
    def statusbar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
    
    def funcTextChanged(self):
        global textChanged
        textChanged = True
        text = self.editor.toPlainText()
        letters = len(text)
        words = len(text.split())
        self.status_bar.showMessage("Number of Letters:  " + str(letters) + "  Number of Words: " + str(words))

    def dockbar(self):
        self.dock = QDockWidget("Shortcuts", self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
        self.dockWidget = QWidget(self)
        self.dock.setWidget(self.dockWidget)
        formLayout = QFormLayout()
        btnFind = QToolButton()
        btnFind.setIcon(QIcon("icons/findlarge.png"))
        btnFind.setText("Find")
        btnFind.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFind.setIconSize(QSize(50, 50))
        btnFind.setCheckable(True)
        btnFind.toggled.connect(self.findEdit)
        btnNew = QToolButton()
        btnNew.setIcon(QIcon("icons/newlarge.png"))
        btnNew.setText("New")
        btnNew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnNew.setIconSize(QSize(50, 50))
        btnNew.setCheckable(True)
        btnNew.toggled.connect(self.newFile)
        btnOpen = QToolButton()
        btnOpen.setIcon(QIcon("icons/openlarge.png"))
        btnOpen.setText("Open")
        btnOpen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnOpen.setIconSize(QSize(50, 50))
        btnOpen.setCheckable(True)
        btnOpen.toggled.connect(self.openFile)
        btnSave = QToolButton()
        btnSave.setIcon(QIcon("icons/newlarge.png"))
        btnSave.setText("Save")
        btnSave.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnSave.setIconSize(QSize(50, 50))
        btnSave.setCheckable(True)
        btnSave.toggled.connect(self.saveFile)
        formLayout.addRow(btnNew, btnOpen)
        formLayout.addRow(btnSave, btnFind)
        self.dockWidget.setLayout(formLayout)

    def toolbar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.changeFont)

        self.tb.addWidget(self.fontFamily)
        self.fontFamily.setCurrentText("Times New Roman")
        self.tb.addSeparator()
        self.fontSize = QComboBox(self)
        self.tb.addWidget(self.fontSize)
        self.fontSize.setEditable(True)
        for i in range(10, 101):
            self.fontSize.addItem(str(i))
        self.fontSize.setCurrentText("12")
        self.fontSize.currentTextChanged.connect(self.changeFontSize)
        self.tb.addSeparator()
        self.bold = QAction(QIcon("icons/bold.png"), "Bold", self)
        self.tb.addAction(self.bold)
        self.bold.triggered.connect(self.Bold)
        self.italic = QAction(QIcon("icons/italic.png"), "Italic", self)        
        self.tb.addAction(self.italic)
        self.italic.triggered.connect(self.Italic)
        self.underline = QAction(QIcon("icons/underline.png"), "Underline", self)
        self.tb.addAction(self.underline)
        self.underline.triggered.connect(self.Underline)
        self.tb.addSeparator()
        ######################################################################
        self.fontColor = QAction(QIcon("icons/color.png"), "Font Color", self)
        self.tb.addAction(self.fontColor)
        self.fontColor.triggered.connect(self.funcFontColor)
        self.fontBackColor = QAction(QIcon("icons/backcolor.png"), "Back Color", self)
        self.tb.addAction(self.fontBackColor)
        self.fontBackColor.triggered.connect(self.funcFontBackColor)
        self.alignLeft = QAction(QIcon("icons/alignleft.png"), "Align Left", self)
        self.tb.addAction(self.alignLeft)
        self.alignLeft.triggered.connect(self.funcAlignLeft)

        self.alignCenter = QAction(QIcon("icons/aligncenter.png"), "Align Center", self)
        self.tb.addAction(self.alignCenter)
        self.alignCenter.triggered.connect(self.funcAlignCenter)

        self.alignRight = QAction(QIcon("icons/alignright.png"), "Align Right", self)
        self.tb.addAction(self.alignRight)
        self.alignRight.triggered.connect(self.funcAlignRight)

        self.alignJustify = QAction(QIcon("icons/alignjustify.png"), "Align Justify", self)
        self.tb.addAction(self.alignJustify)
        self.alignJustify.triggered.connect(self.funcAlignJustify)

        self.tb.addSeparator()
        self.bulletList = QAction(QIcon("icons/bulletlist.png"), "Bullet List", self)
        self.tb.addAction(self.bulletList)
        self.bulletList.triggered.connect(self.funcBulletList)
        self.numList = QAction(QIcon("icons/numberlist.png"), "Numbered List", self)
        self.tb.addAction(self.numList)
        self.numList.triggered.connect(self.funcNumList)
        self.tb.addSeparator()
    def funcBulletList(self):
        self.editor.insertHtml("<ul><li><h4>&nbsp;</h4></li></ul>")
    def funcNumList(self):
        self.editor.insertHtml("<ol><li><h4>&nbsp;</h4></li></ol>")
    def funcAlignLeft(self):
        self.editor.setAlignment(Qt.AlignLeft)
    def funcAlignCenter(self):
        self.editor.setAlignment(Qt.AlignCenter)
    def funcAlignRight(self):
        self.editor.setAlignment(Qt.AlignRight)
    def funcAlignJustify(self):
        self.editor.setAlignment(Qt.AlignJustify)

    def funcFontColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)
    def funcFontBackColor(self):
        bcolor=QColorDialog.getColor()
        self.editor.setTextBackgroundColor(bcolor)

    def Bold(self):
        fontWeight = self.editor.fontWeight()
        if fontWeight ==50:
            self.editor.setFontWeight(QFont.Bold)
        elif fontWeight==75:
            self.editor.setFontWeight(QFont.Normal)
    def Italic(self):
        italic = self.editor.fontItalic()
        if italic == True:
            self.editor.setFontItalic(False)
        else:
            self.editor.setFontItalic(True)
    def Underline(self):
        underline = self.editor.fontUnderline()
        if underline==True:
            self.editor.setFontUnderline(False)
        else:
            self.editor.setFontUnderline(True)


        

    def changeFont(self,font):
        font = QFont(self.fontFamily.currentFont())
        self.editor.setCurrentFont(font)
    
    def changeFontSize(self, fontSize):
        self.editor.setFontPointSize(float(fontSize))
    #################################################################################
    def menu(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        help_menu = menubar.addMenu("Help")

        new = QAction(QIcon("icons/new.png"), "New", self)
        new.setShortcut("Ctrl+N")
        new.triggered.connect(self.newFile)
        file.addAction(new)

        open = QAction(QIcon("icons/open.png"), "Open", self)
        open.setShortcut("Ctrl+O")
        open.triggered.connect(self.openFile)
        file.addAction(open)

        save = QAction(QIcon("icons/save.png"), "Save", self)
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.saveFile)
        file.addAction(save)

        exit = QAction(QIcon("icons/exit.png"), "Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.triggered.connect(self.exitFile)
        file.addAction(exit)

        cut = QAction(QIcon("icons/cut.png"), "Cut", self)
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.cutEdit)
        edit.addAction(cut)

        copy = QAction(QIcon("icons/copy.png"), "Copy", self)
        copy.setShortcut("Ctrl+C")
        copy.triggered.connect(self.copyEdit)
        edit.addAction(copy)

        paste = QAction(QIcon("icons/paste.png"), "Paste", self)
        paste.setShortcut("Ctrl+V")
        paste.triggered.connect(self.pasteEdit)
        edit.addAction(paste)

        undo = QAction(QIcon("icons/undo.png"), "Undo", self)
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.undoEdit)
        edit.addAction(undo)

        find = QAction(QIcon("icons/find.png"), "Find", self)
        find.setShortcut("Ctrl+F")
        find.triggered.connect(self.findEdit)
        edit.addAction(find)

        timedate = QAction(QIcon("icons/time.png"), "Insert Time&Date", self)
        timedate.setShortcut("F5")
        timedate.triggered.connect(self.timeDate)
        edit.addAction(timedate)

        toggleStatusBar = QAction("Toggle Status Bar", self, checkable=True)
        toggleStatusBar.triggered.connect(self.funcToggleStatusBar)
        view.addAction(toggleStatusBar)

        toggleToolBar = QAction("Toggle Tool Bar", self, checkable=True)
        toggleToolBar.triggered.connect(self.funcToggleToolBar)
        view.addAction(toggleToolBar)

        toggleDockBar = QAction("Toggle Dock Bar", self, checkable=True)
        toggleDockBar.triggered.connect(self.functoggleDockBar)
        view.addAction(toggleDockBar)

        aboutus = QAction("About Us", self)
        aboutus.triggered.connect(self.About)
        help_menu.addAction(aboutus)
    
    def newFile(self):
        global url
        try:
            url = ""
            self.editor.clear()      
        except Exception as e:
            print("An error occurred:", str(e))

    def openFile(self):
        global url
        try:
            url, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All File Types (*.*);; txt Files (*.txt)")
            if url:
                with open(url, "r+", encoding="utf-8") as file:
                    content = file.read()
                    self.editor.clear()
                    self.editor.setText(content)
        except Exception as e:
            print("An error occurred:", str(e))
   
    def saveFile(self):
        global url
        try:
            if textChanged:
                if url:
                    content = self.editor.toPlainText()
                    with open(url, "w", encoding="utf-8") as file:
                        file.write(content)
                else:
                    url, _ = QFileDialog.getSaveFileName(self, "Save the File", "", "txt files (*.txt)")
                    if url:
                        content = self.editor.toPlainText()
                        with open(url, "w", encoding="utf-8") as file:
                            file.write(content)
        except Exception as e:
            print("An error occurred:", str(e))

    def exitFile(self):
        global url
        try:
            if textChanged:
                mbox = QMessageBox.question(self, "Warning", "Text was changed, Would you like to save", QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel)
                
                if mbox == QMessageBox.Save:
                    self.saveFile()
                elif mbox == QMessageBox.No:
                    qApp.quit()
            else:
                qApp.quit()      
        except Exception as e:
            print("An error occurred:", str(e))
    
    def cutEdit(self):
        self.editor.cut()

    def copyEdit(self):
        self.editor.copy()

    def pasteEdit(self):
        self.editor.paste()

    def undoEdit(self):
        self.editor.undo()
    
    def findEdit(self):
        self.find = FindDialog()
        self.find.show()

        def findWords():
            try:
                global url
                word = self.find.findInput.text()
                if word:
                    cursor = self.editor.textCursor()
                    format = QTextCharFormat()
                    format.setBackground(QBrush(QColor("yellow")))
                    regex = QRegExp(word)
                    pos = 0
                    index = regex.indexIn(self.editor.toPlainText(), pos)
                    count = 0
                    while index != -1:
                        cursor.setPosition(index)
                        cursor.movePosition(QTextCursor.EndOfWord, 1)
                        cursor.mergeCharFormat(format)
                        pos = index + regex.matchedLength()
                        index = regex.indexIn(self.editor.toPlainText(), pos)
                        count += 1
                    self.status_bar.showMessage(str(count) + " Results Found")
                else:
                    QMessageBox.information(self, "Warning!", "Fields can not be Empty!!!")
            except Exception as e:
                print("An error occurred:", str(e))
        
        def replaceWords():
            try:
                replaceText = self.find.ReplaceInput.text()
                word = self.find.findInput.text()
                if word:
                    text = self.editor.toPlainText()
                    newValue = text.replace(word, replaceText)
                    self.editor.clear()
                    self.editor.append(newValue)
                else:
                    QMessageBox.information(self, "Warning!", "Fields can not be Empty!!!")
            except Exception as e:
                print("An error occurred:", str(e))

        self.find.btnFind.clicked.connect(findWords) 
        self.find.btnReplace.clicked.connect(replaceWords)
    
    def timeDate(self):
        try:
            time_date = time.strftime("%d.%m.%Y %H:%M")
            self.editor.append(time_date)
        except Exception as e:
            print("An error occurred:", str(e))

    def funcToggleStatusBar(self):
        global statusbarchecked
        if statusbarchecked==True:
            self.status_bar.hide()
            statusbarchecked=False
        else:
            self.status_bar.show()
            statusbarchecked=True
    
    def funcToggleToolBar(self):
        global tbchecked
        if tbchecked== True:
           self.tb.hide()
           tbchecked = False
        else:
           self.tb.show()
           tbchecked= True

    
    def functoggleDockBar(self):
        global dockChecked
        if dockChecked == True:
            self.dock.hide()
            dockChecked=False
        else:
            self.dock.show()
            dockChecked=True
    
    
    
    def About(self):
        self.help = about.Help()
        self.help.show()

def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
