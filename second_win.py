# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont

from instr import *
from final_win import *

class Expirement:
    def __init__(self, test1, test2,test3):
        self.test1=test1
        self.test2=test2
        self.test3=test3
        

class TestWin(QWidget):
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
        self.name=QLabel(txt_name) 
        self.name_editor=QLineEdit()
        self.age=QLabel(txt_age)
        self.age_editor=QLineEdit()     
        self.instr1=QLabel(txt_test1)   
        self.btn1=QPushButton(txt_starttest1)
        self.test1=QLineEdit()
        self.instr2=QLabel(txt_test2)   
        self.btn2=QPushButton(txt_starttest2)
        self.instr3=QLabel(txt_test3)   
        self.btn3=QPushButton(txt_starttest3)
        self.test2=QLineEdit()
        self.test3=QLineEdit()
        self.btn_res=QPushButton(txt_sendresults)

        self.timer_txt=QLabel('00:00:00')
        self.timer_txt.setFont(QFont("Times",36,QFont.Bold))

        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.h_line=QHBoxLayout()

        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.name_editor, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age_editor, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instr1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instr2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instr3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_res, alignment = Qt.AlignRight)

        self.r_line.addWidget(self.timer_txt, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    def timer_test1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.timer_txt.setText(time.toString('hh:mm:ss'))
        if (time.toString('hh:mm:ss'))=='00:00:00':
            self.timer.stop()
    def timer_test2(self):
        global time
        time = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer2Event(self):
        global time
        time=time.addSecs(-1)
        self.timer_txt.setText(time.toString('hh:mm:ss'))
        if (time.toString('hh:mm:ss'))=='00:00:00':
            self.timer.stop()

    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time=time.addSecs(-1)
        self.timer_txt.setText(time.toString('hh:mm:ss'))
        t1=time.toString('hh:mm:ss')
        t2=int(t1[6:8])
        if t2>15 and t2<45:
            self.timer_txt.setStyleSheet('color:rgb(0,0,0)')
        else:
            self.timer_txt.setStyleSheet('color:rgb(0,255,0)')

        if (time.toString('hh:mm:ss'))=='00:00:00':
            self.timer.stop()

    def connects(self):
        self.btn_res.clicked.connect(self.next_click)
        self.btn1.clicked.connect(self.timer_test1)
        self.btn2.clicked.connect(self.timer_test2)
        self.btn3.clicked.connect(self.timer_test3)

    def next_click(self):
        self.hide()
        ts1=int(self.test1.text())
        ts2=int(self.test2.text())
        ts3=int(self.test3.text())
        self.exp1=Expirement(ts1,ts2,ts3)
        #print(self.test1.text(), self.test2.text(), self.test3.text())
        self.fw=FinalWin(self.exp1)   
