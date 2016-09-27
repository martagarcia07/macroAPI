# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import os
import sys
import constants
import datetime
import json
from pymongo import MongoClient

# 1g Protein = 4 Calories
# 1g Carbohydrate = 4 Calories
# 1g Fat = 9 Calories

class macroCalculation:
    def __init__(self, weight,height, age, gender,activityLevel,goal,userId):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.gender = gender
        self.activityLevel = activityLevel
        self.macros= dict()    
        self.goal=goal    
        self.userId=userId
    def macroCalculations(self):
        if self.gender==constants.MALE:
            REE=10*self.weight + 6.25*self.height - 5*self.age + 5
        elif self.gender==constants.FEMALE:
            REE=10*self.weight + 6.25*self.height - 5*self.age + 5 - 161
        if self.activityLevel==constants.SEDENTARY:
            TDEE=REE*1.2
        elif self.activityLevel==constants.LIGHT:
            TDEE=REE*1.375
        elif self.activityLevel==constants.MODERATE:
            TDEE=REE*1.55
        elif self.activityLevel==constants.ACTIVE:
            TDEE=REE*1.725
        if self.goal==constants.MASSGAIN:
            cal_intake=TDEE*1.2
            fat_cal_intake=cal_intake*0.2
            pro_cal_intake=cal_intake*0.35
            car_cal_intake=cal_intake*0.45
        elif self.goal==constants.FATLOSS:
            cal_intake=TDEE*0.8
            fat_cal_intake=cal_intake*0.2
            pro_cal_intake=cal_intake*0.4
            car_cal_intake=cal_intake*0.4
        elif self.goal==constants.MANTAIN:
            cal_intake=TDEE
            fat_cal_intake=cal_intake*0.25
            pro_cal_intake=cal_intake*0.3
            car_cal_intake=cal_intake*0.45
        fat_gr_intake=fat_cal_intake/9
        pro_gr_intake=pro_cal_intake/4
        car_gr_intake=car_cal_intake/4   
        self.macros["cal_intake"]=cal_intake
        self.macros["fat_gr_intake"]=fat_gr_intake
        self.macros["pro_gr_intake"]=pro_gr_intake
        self.macros["car_gr_intake"]=car_gr_intake
        self.macros["date"]=datetime.datetime.now().isoformat()
        #source_dir= "./tmp"
        #fileName=source_dir+"/"+datetime.datetime.now().isoformat().replace('-','').replace(':','').replace('.','')+'_'
        #if not os.path.exists(source_dir) :
        #    os.makedirs(source_dir)
        #json.dump(self.macros, open(fileName+self.userId, 'w'))
        db = MongoClient('localhost', 27017) 
        db.userMacros[self.userId].insert_many([self.macros])
        
