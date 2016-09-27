# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import os
import sys
import constants
import datetime
import json
import psycopg2
from passlib.hash import sha256_crypt

# 1g Protein = 4 Calories
# 1g Carbohydrate = 4 Calories
# 1g Fat = 9 Calories

class registerUser:
    def __init__(self, username,password, name, surname,birthdate,email):
        self.username = username
        self.password = sha256_crypt.encrypt(password)
        self.name = name
        self.surname = surname
        self.last_online = datetime.datetime.now().isoformat()
        self.birthdate = birthdate
        self.email = email
    def registration(self):
        try:
            varString="'"+self.username+"','"+self.password+"','"+self.name+"','"+self.surname+"','"+self.last_online+"','"+self.birthdate+"','"+self.email+"'"
            conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
            cur = conn.cursor()
            try:
                cur.execute("insert into users_db (username,pass,name,surname,last_online,birthdate,email)values ("+varString+");")
                cur.execute("commit;")
            except:
                conn.rollback()
                print "wrong values"

        except:
            conn.rollback()
            print "Unable to connect to the database"

