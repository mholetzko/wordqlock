# -*- coding: utf-8 -*-

import datetime as t

class wordqlockTimeHandler():
    
    def __init__(self):
        self.currentTime = t.datetime.now();
        self.activeIndices = [];

        
    def updateTime(self):
        self.currentTime = t.datetime.now();

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
        self.updateTime()
        uIdx = 0;
        for i in range(len(self.minutecfgs) - 1 ):
            if self.currentTime.minute >= self.minutecfgs[i][1] and self.currentTime.minute < self.minutecfgs[i+1][1]:
                   
                #print("INDEX" + str(i) + self.minutecfgs[i][0]);
                uIdx = i;

        return self.minutecfgs[uIdx][2]

    def getCurrentHourCfg(self):
        self.updateTime()
        table = self.hourcfgs[self.getTableTime(self.currentTime.hour)][2]
        #todo handle special case EIN(S)
        if self.currentTime.minute < 5 and self.currentTime.hour == 1:
            table = table[:-1];
        return table
        
    def getCurrentMinuteOffset(self):
        self.updateTime()
        offset = 0;
        for i in range(len(self.minutecfgs) - 1 ):
            if self.currentTime.minute >= self.minutecfgs[i][1] and self.currentTime.minute < self.minutecfgs[i+1][1]:
                   
                #print("INDEX" + str(i) + self.minutecfgs[i][0]);
                offset = self.currentTime.minute - self.minutecfgs[i][1];
        #print(offset)
        return [x for x in range(offset)]

    def getCurrentSecondOffset(self):
        self.updateTime()
        return self.currentTime.second

    def setActiveByIndex(self,row,col):
        
        bRet = False;
        for (i,j) in self.staticIndices:
            if i == row and j == col:
                #print(self.currentTime)
                bRet = True;
        #todo check for special cases
        for (m,n) in self.getCurrentMinuteCfg():
             if m == row and n == col:
                #print(self.currentTime)
                bRet = True;
                
        for (p,q) in self.getCurrentHourCfg():
             if p == row and q == col:
                #print(self.currentTime)
                bRet = True;
        
        if self.currentTime.minute < 5:
            #print UHR
            if row == 9 and col in [8,9,10]:
                bRet = True;
        return bRet;

        
        
        
        
     
        
        