# -*- coding: utf-8 -*-

from layout import WqLayout
import datetime as t

class WqTimeHandler(WqLayout):
    
    def __init__(self):
        
        super().__init__()
        self.currentTime    = t.datetime.now();
        self.activeIndices  = [];
        self.fakeTime       = False;

    def updateTime(self):
        if not(self.fakeTime):
            self.currentTime = t.datetime.now()
        else:  
            self.currentTime = self.currentTime + t.timedelta(minutes=5);

    def getTableTime(self,hour):
        if self.currentTime.minute >= 25:
            if hour < 24:
                lochour = hour + 1
            else:
                lochour = 0
            return lochour%12;
        else:
            return hour%12;
                

    def getCurrentMinuteCfg(self):
        
        uIdx = 0;
        minCfg = self.getMinuteCfg();

        for i in range(len(minCfg) - 1 ):
            if self.currentTime.minute >= minCfg[i][1] and self.currentTime.minute < minCfg[i+1][1]:
                   
                #print("INDEX" + str(i) + self.minutecfgs[i][0]);
                uIdx = i;

        return minCfg[uIdx][2]

    def getCurrentHourCfg(self):
        
        hourCfg = self.getHourCfg();

        table = hourCfg[self.getTableTime(self.currentTime.hour)][2]
        #todo handle special case EIN(S)
        if self.currentTime.minute < 5 and self.currentTime.hour == 1:
            table = table[:-1];
        return table
        
    def getCurrentMinuteOffset(self):
        
        offset = 0;
        minCfg = self.getMinuteCfg();

        for i in range(len(minCfg) - 1 ):
            if self.currentTime.minute >= minCfg[i][1] and self.currentTime.minute < minCfg[i+1][1]:
                offset = self.currentTime.minute - minCfg[i][1];
        return [x for x in range(offset)]

    def getCurrentSecondOffset(self):
        
        return self.currentTime.second

    def getActiveByTable(self,table,row,col,pred):
        uRet = 0;
        if pred:
            for (i,j) in table:
                if i == row and j == col:
                    uRet = 1;
        return uRet;
        
    def setActiveByIndex(self,row,col):
        
        bRet = False;
        uRet = 0;
        uRet = uRet + self.getActiveByTable(self.getStaticIndices()   ,row,col,True);
        uRet = uRet + self.getActiveByTable(self.getCurrentMinuteCfg(),row,col,True);
        uRet = uRet + self.getActiveByTable(self.getCurrentHourCfg()  ,row,col,True);
        uRet = uRet + self.getActiveByTable(self.getOclockIndices()   ,row,col,(self.currentTime.minute < 5));
        uRet = uRet + self.getActiveByTable(self.getamIndices()       ,row,col,(self.currentTime.hour   <= 12));
        uRet = uRet + self.getActiveByTable(self.getpmIndices()       ,row,col,(self.currentTime.hour   >  12));

        if uRet > 0:
            bRet = True;
            
        return bRet;

        
        
        
        
     
        
        