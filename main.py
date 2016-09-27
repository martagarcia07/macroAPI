# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import os
import sys
lib_path = os.path.abspath(os.path.join( 'lib','var'))
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


source_dir= "./tmp"
fileName=source_dir+"/file"
######################################################## MAIN ##################################################################
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == constants.CODE1 and len(sys.argv)==9:
            try:
                #weight,height, age, gender,activityLevel,goal, user_id
                userMacros = macroCalculation(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
                userMacros.macroCalculations()
                if not os.path.exists(source_dir) :
                    os.makedirs(source_dir)
                json.dump(userMacros.macros, open(fileName+sys.argv[8], 'w'))
            except:
                print "do something when wrong parameters"
            ## userMacros.macros --->{'car_gr_intake': 168.51600000000005, 'cal_intake': 1685.1600000000003, 
            ## 'fat_gr_intake': 37.44800000000001, 'pro_gr_intake': 168.51600000000005}

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
####################################################### END MAIN ################################################################