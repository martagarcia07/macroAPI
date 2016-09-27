# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import os
import sys
lib_path = os.path.abspath(os.path.join( './var'))
sys.path.append(lib_path)
lib_path = os.path.abspath(os.path.join( './lib'))
sys.path.append(lib_path)

import numpy as np
import json

import datetime
from datetime import timedelta
import time
import re

import constants
from macroCalculation import macroCalculation
from fitMacros import fitMacros,recalculateMacros
from insertMacrosDB import insertMacrosDB
from registerUser import registerUser

source_dir= "./tmp"
fileName=source_dir+"/file"
######################################################## MAIN ##################################################################
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == constants.CODE1 and len(sys.argv)==9:
            try:
                #weight,height, age, gender,activityLevel,goal, user_id
                userMacros = macroCalculation(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
                userMacros.macroCalculations()
            except:
                print "do something when wrong parameters"            
            #userMacros.macros['car_gr_intake']
        elif sys.argv[1] == constants.CODE2 and len(sys.argv)>=4 and os.path.exists(fileName+sys.argv[2]):
            # user_id,workOut,json
            if len(sys.argv)==5:
                recalculateMacros(sys.argv[2],sys.argv[3],sys.argv[4])
            elif len(sys.argv)==4:
                m=fitMacros(sys.argv[2],sys.argv[3])
                m.macroCalculations()
        elif sys.argv[1] == constants.CODE3 and len(sys.argv)==11:
            ### 2-10 product, producto,cal,fat,pro,car,porttype,port,types
            insertMacrosDB(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10])
        elif sys.argv[1] == constants.CODE4 and len(sys.argv)==8:
            newUser=registerUser(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
            newUser.registration()
            #  username,password, name, surname,birthdate(2016,2,1),email

####################################################### END MAIN ################################################################