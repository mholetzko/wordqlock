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
        self.intensity = 250
        self.process()
        self.offset_canvas = self.matrix.CreateFrameCanvas()

    def setBitMapForShiftingReg(self,bitMapId, bit):
        self.bitMapSReg[bitMapId][bit] = 1

    def resetBitMapForShiftingReg(self,bitMapId,bit):
        self.bitMapSReg[bitMapId][bit] = 0
            
    def printBitMapForShiftingReg(self):
        if self.debug:
            rowIdx = 0
            for row in self.bitMapSReg:
                pixlIdx = 0
                for pixel in row:
                    if pixel != 0:
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx,      2*rowIdx+rowIdx,self.intensity,self.intensity,self.intensity)
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx+1,    2*rowIdx+rowIdx,self.intensity,self.intensity,self.intensity)
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx,      2*rowIdx+rowIdx+1,self.intensity,self.intensity,self.intensity)
                        self.offset_canvas.SetPixel(2*pixlIdx+pixlIdx+1,    2*rowIdx+rowIdx+1,self.intensity,self.intensity,self.intensity)
                    pixlIdx = pixlIdx + 1
                rowIdx = rowIdx + 1
            self.matrix.Clear()
            self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)

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
        self.setLetterBitValues()
        time.sleep(0.01)


if __name__ == '__main__':
    
    app = wqTargetApp(1)
    
    while True:
        try:
            # Start loop
            app.run()
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

