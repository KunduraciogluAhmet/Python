import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

result=0
result_list=[]

class Calculator (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator by AKo")
        self.setGeometry(350,100,380,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):
        ######### EntryBox ###############

        self.entry_box= QLineEdit(self)
        self.entry_box.resize(335,30)
        self.entry_box.setAlignment(Qt.AlignRight)
        self.entry_box.setStyleSheet("font: 14pt Arial Bold; border:3px solid gray; border-radius:10px; background-color:#e6e6ef")
        self.entry_box.setText("O")
        self.entry_box.move(20,30)
        ############################ number buttons #####################
        btn_number=[]
        for i in range(1,10):
            i= QPushButton(str(i),self)
            i.setFont(QFont("Arial", 15))
            i.resize(70,40)
            i.setStyleSheet("background-color:#fff")
            i.clicked.connect(self.enterNumbers)
            btn_number.append(i)

        btn_index=0
        for i in range(0,3):
            for j in range(0,3):
                btn_number[btn_index].move(25+j*90, 70+i*70)
                btn_index +=1

        ################## Operator Buttons #####################
        btn_operator =[]
        for i in range(4):
            i=QPushButton(self)
            i.resize(70,40)
            i.setStyleSheet("background-color:#deedaf")
            i.setFont(QFont("Arial",15))
            i.clicked.connect(self.enterOperator)
            btn_operator.append(i)
        btn_operator[0].setText("+")
        btn_operator[1].setText("-")
        btn_operator[2].setText("*")
        btn_operator[3].setText("/")

        for i in range(4):
            btn_operator[i].move(290,(i+1)*70)

        ##################### Other Buttons ###########################
        btn_zero= QPushButton("0",self)
        btn_zero.setStyleSheet("background-color:#fff")
        btn_zero.setFont(QFont("Arial", 20))
        btn_zero.resize(250,40)
        btn_zero.clicked.connect(self.enterNumbers)
        btn_zero.move(25,280)

        btn_clear=QPushButton("C",self)
        btn_clear.setStyleSheet("background-color:#f99")
        btn_clear.setFont(QFont("Arial", 20))
        btn_clear.resize(70,40)
        btn_clear.clicked.connect(self.funcClear)
        btn_clear.move(25,340)

        btn_dot=QPushButton(".",self)
        btn_dot.setStyleSheet("background-color:#f99")
        btn_dot.setFont(QFont("Arial", 15))
        btn_dot.resize(70,40)
        btn_dot.clicked.connect(self.enterNumbers)
        btn_dot.move(115,340)

        btn_equal=QPushButton("=",self)
        btn_equal.setStyleSheet("background-color:#f99")
        btn_equal.setFont(QFont("Arial", 20))
        btn_equal.resize(70,40)
        btn_equal.clicked.connect(self.funcResult)
        btn_equal.move(205,340)

        btn_del=QPushButton(self)
        btn_del.setStyleSheet("background-color:#fff")
        btn_del.setIcon(QIcon("icons/Arrowback48.png"))
        btn_del.resize(70,40)
        btn_del.clicked.connect(self.funcDelete)
        btn_del.move(290,340)
    #############Status Bar######################
        self.status_bar= QStatusBar()
        self.setStatusBar(self.status_bar)

    def enterNumbers(self):
        btn_text=self.sender().text()
        if self.entry_box.text()=="O":
            self.entry_box.setText(btn_text)
        else:
            self.entry_box.setText(self.entry_box.text()+btn_text)

    def enterOperator(self):
        btn_text=self.sender().text()
        if self.entry_box.text() !="O":
            self.entry_box.setText(self.entry_box.text()+btn_text)

    def funcClear(self):
        self.entry_box.setText("O")
    
    def funcDelete(self):
        x=self.entry_box.text()
        x=x[:-1]
        self.entry_box.setText(x)
        if len(x) ==0:
            self.entry_box.setText("O")
    
    def funcResult(self):
        content=self.entry_box.text()
        result=eval(content)
        self.entry_box.setText(str(result))

        result_list.append(content)
        result_list.reverse()
        self.status_bar.showMessage("History: " + "|".join(result_list[:5]))
        self.status_bar.setFont(QFont("Verdana", 15))
    

def main():
    App=QApplication(sys.argv)
    Window= Calculator()
    sys.exit(App.exec_())

if __name__== "__main__":
    main()


