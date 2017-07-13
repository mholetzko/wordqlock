# -*- coding: utf-8 -*-

from timeHandler import wordqlockTimeHandler

class wordqlockLayout(wordqlockTimeHandler):
    
    def __init__(self):
        super().__init__()
        
        self.letterField = [];
        self.letterField.append(["E","S","K","I","S","T","A","F","U","N","F"])
        self.letterField.append(["Z","E","H","N","Z","W","A","N","Z","I","G"])
        self.letterField.append(["D","R","E","I","V","I","E","R","T","E","L"])
        self.letterField.append(["V","O","R","F","U","N","K","N","A","C","H"])
        self.letterField.append(["H","A","L","B","A","E","L","F","U","N","F"])
        self.letterField.append(["E","I","N","S","X","A","M","Z","W","E","I"])
        self.letterField.append(["D","R","E","I","P","M","J","V","I","E","R"])
        self.letterField.append(["S","E","C","H","S","B","L","A","C","H","T"])
        self.letterField.append(["S","I","E","B","E","N","Z","W","O","L","F"])
        self.letterField.append(["Z","E","H","N","E","U","N","K","U","H","R"])
        
        self.staticIndices = [(0,0),(0,1),(0,3),(0,4),(0,5)];
        self.oclockIndices = [(9,8),(9,9),(9,10)];
        
        #The first  triple element is soley for debugging and printing purpose
        #The second triple element is denoting the discretizied minute position where we wanna have transitions
        #The third  triple element is giving tuples of active coordinates 
        self.minutecfgs = [ ['VOLL     '       ,0 ,[(9,8),(9,9),(9,10)]],
                            ['FUENFNACH'       ,5 ,[(0,7),(0,8),(0,9),(0,10),(3,7),(3,8),(3,9),(3,10)]],
                            ['ZEHNNACH'        ,10,[(1,0),(1,1),(1,2),(1,3),(3,7),(3,8),(3,9),(3,10)]],
                            ['VIERTELNACH'     ,15,[(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,7),(3,8),(3,9),(3,10)]],
                            ['ZWANZIGNACH'     ,20,[(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(3,7),(3,8),(3,9),(3,10)]],
                            ['FUNFVORHALB'     ,25,[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3),(0,7),(0,8),(0,9),(0,10)]],
                            ['HALB'            ,30,[(4,0),(4,1),(4,2),(4,3)]],
                            ['FUNEFNACHHALB'   ,35,[(0,7),(0,8),(0,9),(0,10),(4,0),(4,1),(4,2),(4,3),(3,7),(3,8),(3,9),(3,10)]],
                            ['ZWANZIGVOR'      ,40,[(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(3,0),(3,1),(3,2)]],
                            ['VIERTELVOR'      ,45,[(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,0),(3,1),(3,2)]],
                            ['ZEHNVOR'         ,50,[(1,0),(1,1),(1,2),(1,3),(3,0),(3,1),(3,2)]],
                            ['FUENFVOR'        ,55,[(3,0),(3,1),(3,2),(0,7),(0,8),(0,9),(0,10)]],
                            ['VOLL    '        ,60,[(9,8),(9,9),(9,10)]]]
                     
        #The first  triple element is soley for debugging purpose
        #the second triple elmenet is denoting the hour in (am,pm)-style
        #  --> 0-23 hours style % 12 is resulting in this
        #the third  triple element is giving tuples of active coordinates
        self.hourcfgs   = [ ['ZWOLF     '       ,0 ,[(8,6),(8,7),(8,8),(8,9),(8,10)]],
                            ['EINS'             ,1 ,[(5,0),(5,1),(5,2),(5,3)]],
                            ['ZWEI'             ,2,[(5,7),(5,8),(5,9),(5,10)]],
                            ['DREI'             ,3,[(6,0),(6,1),(6,2),(6,3)]],
                            ['VIER'             ,4,[(6,7),(6,8),(6,9),(6,10)]],
                            ['FUNF'             ,5,[(4,7),(4,8),(4,9),(4,10)]],
                            ['SECHS'            ,6,[(7,0),(7,1),(7,2),(7,3),(7,4)]],
                            ['SIEBEN'           ,7,[(8,0),(8,1),(8,2),(8,3),(8,4),(8,5)]],
                            ['ACHT'             ,8,[(7,7),(7,8),(7,9),(7,10)]],
                            ['NEUN'             ,9,[(9,3),(9,4),(9,5),(9,6)]],
                            ['ZEHN'             ,10,[(9,0),(9,1),(9,2),(9,3)]],
                            ['ELF'              ,11,[(4,5),(4,6),(4,7)]]]

    def getLetterField(self):
        return self.letterField;
