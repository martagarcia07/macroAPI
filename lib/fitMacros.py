# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import constants
from astropy.table import Table, Column
from astropy import units as u
import json
import psycopg2
from pymongo import MongoClient
from bson.objectid import ObjectId

class fitMacros:
    def __init__(self,user_id,workout):
        db = MongoClient('localhost', 27017) 
        #source_dir= "./tmp"
        #fileName=source_dir+"/file"
        #self.macros = json.load(open(fileName+user_id))
        self.userId = user_id   
        self.macros = db.userMacros[self.userId].find()
        self.workout=workout
        self.table = Table(names=('h', 'g', 'p', 'fch', 'sch'), dtype=('S2', 'f4', 'f4', 'f4', 'f4'))
        print self.macros[0]
        for item in  self.macros[0]:
            exec("self."+item+"= self.macros[0][item]")

    def macroCalculations(self):
        try:
            conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
        except:
            print "I am unable to connect to the database"
        # if int(self.macros['car_gr_intake'])==int(self.macros['pro_gr_intake']):
        #     if self.workout == constants.AFTERNOON:
        #         self.table.add_row(("first",4.12,11.76,7.06,7.76))
        #         self.table.add_row(("second",0,10.59,0,0))
        #         self.table.add_row(("third",0,5.18,0,10.59))
        #         self.table.add_row(("fourth",0,3.53,7.06,15.29))
        #         self.table.add_row(("fifth",0,11.76,0,5.88))
        #     elif self.workout == constants.MORNING:
        #         self.table.add_row(("first",4.12,5.88,7.06,1.53))
        #         self.table.add_row(("second",0,10.59,0,5.88))
        #         self.table.add_row(("third",0,11.06,0,10.59))
        #         self.table.add_row(("fourth",0,3.53,7.06,3.53))
        #         self.table.add_row(("fifth",0,6.76,0,5.88))
        #     print self.table


class recalculateMacros:
    def __init__(self,user_id, workout, json):
        self.weight = float(weight)
    #def macroCalculations(self):
        
