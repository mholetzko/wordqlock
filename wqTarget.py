#!/usr/bin/env python
#common
import time
import datetime as t
import sys
#rgb matrix modules
try:
    from samplebase import SampleBase
    from rgbmatrix import graphics
except:
    print("install libraries")

from wqTime2LayoutWrapper import WqTime2LayoutHandler

class wqTargetApp():

    def __init__(self,updatePeriod):
        self.timeHandler = WqTime2LayoutHandler()
        self.bitMapSReg = [[x for x in range(11)] for x in range(10)]
        self.debug = True
        self.period = updatePeriod
        self.init = False

    def runApp(self):

       pass
                
    def setBitMapForShiftingReg(self,bitMapId, bit):
        self.bitMapSReg[bitMapId][bit] = 1

    def resetBitMapForShiftingReg(self,bitMapId,bit):
        self.bitMapSReg[bitMapId][bit] = 0
            
    def printBitMapForShiftingReg(self):
        if self.debug:
            print(" ### Mask For Shifting Registers ###")
            for x in self.bitMapSReg:
                print(x)
            print(" \n")

    def setLetterBitValues(self):
        self.timeHandler.updateTime()
        
        for i in range(self.timeHandler.getLetterFieldRowSize()):
            for j in range(self.timeHandler.getLetterFieldColSize(i)):
                #Here we would set the shift registers!!!!!
                self.resetBitMapForShiftingReg(i,j)
                if(self.timeHandler.setActiveByIndex(i,j)):
                    self.setBitMapForShiftingReg(i,j)       
        self.printBitMapForShiftingReg()
       

    def run(self):
        if self.init and self.timeHandler.getTimeSinceLastUpdate() < t.timedelta(minutes=self.period):
            print(" ### Wait for "+str(self.period)+" minutes ###")
            time.sleep(self.period*100)
        else:
            self.init = True
            self.setLetterBitValues()


if __name__ == '__main__':
    
    app = wqTargetApp(1)
    
    while True:
        app.run()