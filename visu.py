#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
"""

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QTimer

from layout      import wordqlockLayout

class WordqlockVisu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.timer = QTimer(); 
        self.timer.setInterval(1000)
        self.initUI()
        
        
    def initUI(self):      

        self.layout = wordqlockLayout();
        self.setStyleSheet("background-color: black")
        self.setGeometry(100, 100, 220, 250)
        self.setWindowTitle('WordQlockLayout')  
        self.timer.timeout.connect(self.update)
        self.timer.start();

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        self.drawRectangle(qp)
        qp.end()
        
    def drawRectangle(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setOpacity(0.25)
        qp.setBrush(Qt.darkGray)
        qp.drawRect(10, 10, 200, 230)
        for x in self.layout.getCurrentMinuteOffset():
            qp.setBrush(Qt.red)
            qp.drawRect(15 + x*60, 15, 10, 10)
        qp.setBrush(Qt.red)
        qp.drawRect(15, 220, 10+ 3*self.layout.getCurrentSecondOffset(), 10)
            

        
    def drawText(self, event, qp):
        offset = 3;
        offsety = 3;
        self.layout.updateTime()
        for i in range(len(self.layout.letterField)):
            offsety +=10;
            offset = 3;
            for j in range(len(self.layout.letterField[i])):
                #Here we would set the shift registers!!!!!
                #and illuminate the output
                offset += 10; 
                if(self.layout.setActiveByIndex(i,j)):
                    qp.setPen(Qt.white)
                else:
                    qp.setPen(Qt.darkGray)
                qp.setFont(QFont('Decorative', 10))
                qp.drawText(5+offset ,10+offsety, 20+offset, 30+offsety, Qt.AlignCenter, self.layout.letterField[i][j])        


    def update(self):
        self.repaint()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = WordqlockVisu()
    ex.show()
    sys.exit(app.exec_())