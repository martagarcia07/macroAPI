# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import constants
from astropy.table import Table, Column
from astropy import units as u
import json

class fitMacros:
    def __init__(self,user_id,workout):
        source_dir= "./tmp"
        fileName=source_dir+"/file"
        self.macros = json.load(open(fileName+user_id))
        self.workout=workout
        self.table = Table(names=('h', 'g', 'p', 'fch', 'sch'), dtype=('S2', 'f4', 'f4', 'f4', 'f4'))

        
    def macroCalculations(self):
        if int(self.macros['car_gr_intake'])==int(self.macros['pro_gr_intake']):
            if self.workout == constants.AFTERNOON:
                self.table.add_row(("first",4.12,11.76,7.06,7.76))
                self.table.add_row(("second",0,10.59,0,0))
                self.table.add_row(("third",0,5.18,0,10.59))
                self.table.add_row(("fourth",0,3.53,7.06,15.29))
                self.table.add_row(("fifth",0,11.76,0,5.88))
            elif self.workout == constants.MORNING:
                self.table.add_row(("first",4.12,5.88,7.06,1.53))
                self.table.add_row(("second",0,10.59,0,5.88))
                self.table.add_row(("third",0,11.06,0,10.59))
                self.table.add_row(("fourth",0,3.53,7.06,3.53))
                self.table.add_row(("fifth",0,6.76,0,5.88))
        	print self.table


class recalculateMacros:
    def __init__(self,user_id, workout, json):
        self.weight = float(weight)
    #def macroCalculations(self):
        
