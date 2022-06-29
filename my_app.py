# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.hello_txt=QLabel(txt_hello)         #для текста добро пожаловать
        self.instruction=QLabel(txt_instruction) # для текста инструкции
        self.button=QPushButton(txt_next)        # для кнопки "начать"

        self.Vlayout=QVBoxLayout()   # для вертикального расположение виджетов 
        ''' добавление в вертикальное расположение виджетов '''
        self.Vlayout.addWidget(self.hello_txt)
        self.Vlayout.addWidget(self.instruction)
        self.Vlayout.addWidget(self.button) 

        self.setLayout(self.Vlayout) # установить расположение для окна 


    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw=TestWin()    


app=QApplication([])
main_win=MainWin()
app.exec_()
