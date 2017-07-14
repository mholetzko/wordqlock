#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
"""

import sys
from PyQt5.QtWidgets    import QApplication,QMainWindow
from PyQt5.QtGui        import QPainter, QColor, QFont
from PyQt5.QtCore       import Qt, QTimer

from time2LayoutWrapper import WqTimeHandler

class WordqlockVisu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.timer = QTimer(); 
        self.timer.setInterval(500)
        self.initUI()
        self.debug      = False
        self.bitMapSReg = [[x for x in range(11)] for x in range(10)]
        
        
    def initUI(self):      

        self.timeHandler = WqTimeHandler();
        self.setStyleSheet("background-color: black")
        self.setGeometry(100, 100, 220, 250)
        self.setWindowTitle('WordQlocktimeHandler')  
        self.timer.timeout.connect(self.update)
        self.timer.start();

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.setLetterBitValues(event, qp)
        self.drawRectangles(qp)
        qp.end()
        
    def drawTimeBoxes(self,qp):
        for x in self.timeHandler.getCurrentMinuteOffset():
            qp.setBrush(Qt.red)
            qp.drawRect(15 + x*60, 15, 10, 10)
        qp.setBrush(Qt.red)
        qp.drawRect(15, 220, 10+ 3*self.timeHandler.getCurrentSecondOffset(), 10)
        
    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setOpacity(0.25)
        qp.setBrush(Qt.darkGray)
        qp.drawRect(10, 10, 200, 230)
        self.drawTimeBoxes(qp)
            
    def setBitMapForShiftingReg(self,bitMapId, bit):
        self.bitMapSReg[bitMapId][bit] = 1;

    def resetBitMapForShiftingReg(self,bitMapId,bit):
        self.bitMapSReg[bitMapId][bit] = 0;
        
    def printBitMapForShiftingReg(self):
        if self.debug:
            print(" ### Mask For Shifting Registers ###")
            for x in self.bitMapSReg:
                print(x)
            print(" \n")

    def setLetterBitValues(self, event, qp):
        offset  = 3;
        offsety = 3;
        self.timeHandler.updateTime()
        
        for i in range(self.timeHandler.getLetterFieldRowSize()):
            offsety +=10;
            offset = 3;
            for j in range(self.timeHandler.getLetterFieldColSize(i)):
                #Here we would set the shift registers!!!!!
                #and illuminate the output
                offset += 10; 
                self.resetBitMapForShiftingReg(i,j)
                if(self.timeHandler.setActiveByIndex(i,j)):
                    qp.setPen(Qt.white)
                    self.setBitMapForShiftingReg(i,j)
                else:
                    qp.setPen(Qt.darkGray)
                qp.setFont(QFont('Decorative', 10))
                qp.drawText(5+offset ,10+offsety, 20+offset, 30+offsety, Qt.AlignCenter, self.timeHandler.letterField[i][j])        
        self.printBitMapForShiftingReg()

    def update(self):
        self.repaint()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = WordqlockVisu()
    ex.show()
    sys.exit(app.exec_())