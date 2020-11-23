#!/usr/bin/env python
#common
import time
import datetime as t
import sys
#rgb matrix modules
try:
    from samplebase import SampleBase
except:
    print("install libraries")

from wqTime2LayoutWrapper import WqTime2LayoutHandler

class wqTargetApp(SampleBase):
        
    def __init__(self,updatePeriod,*args, **kwargs):
        super(wqTargetApp, self).__init__(*args, **kwargs)
        self.timeHandler = WqTime2LayoutHandler()
        self.bitMapSReg = [[x for x in range(11)] for x in range(10)]
        self.debug = True
        self.period = updatePeriod
        self.init = False
        self.intensity = 50
        sys.argv.append("-p 1")
        self.process()
        self.offset_canvas = self.matrix.CreateFrameCanvas()

    def setBitMapForShiftingReg(self,bitMapId, bit):
        self.bitMapSReg[bitMapId][bit] = 1

    def resetBitMapForShiftingReg(self,bitMapId,bit):
        self.bitMapSReg[bitMapId][bit] = 0
            
    def printBitMapForShiftingReg(self):
        if self.debug:
            self.matrix.Clear()
            print(" ### Mask For Shifting Registers ###")
            rowIdx = 0
            for row in self.bitMapSReg:
                print(row)
                pixlIdx = 0
                for pixel in row:
                    if pixel != 0:
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx,      2*rowIdx+rowIdx,self.intensity,self.intensity,self.intensity)
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx+1,    2*rowIdx+rowIdx,self.intensity,self.intensity,self.intensity)
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx,      2*rowIdx+rowIdx+1,self.intensity,self.intensity,self.intensity)
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx+1,    2*rowIdx+rowIdx+1,self.intensity,self.intensity,self.intensity)
                    pixlIdx = pixlIdx + 1
                rowIdx = rowIdx + 1
            self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)

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
        try:
            # Start loop
            app.run()
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

