# -*- coding: utf-8 -*-
__author__ = 'Meekooloh'

import constants
from astropy.table import Table, Column
from astropy import units as u
import json
import psycopg2

class insertMacrosDB:
    def __init__(self, product, producto,cal,fat,pro,car,porttype,port,types):
        try:
            varString=",'"+product+"','"+producto+"',"+cal+","+fat+","+pro+","+car+",'"+porttype+"',"+port+",'"+types+"'" 
            ###",'oat','avena',389,7,17,66,'g',100,'sch'"
            conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
            cur = conn.cursor()
            cur.execute("select max(id)  from macros_db ")
            rows = cur.fetchall()
            newId=rows[0][0]+1
            try:
                cur.execute("INSERT INTO macros_db (id,product,producto,cal,fat,pro,car,porttype,port,type) VALUES ("+str(newId)+varString+");")            

                cur.execute("commit;")
            except:
                print "INSERT INTO macros_db (id,product,producto,cal,fat,pro,car,porttype,port,type) VALUES ("+str(newId)+varString+");"
                conn.rollback()
                print "wrong values"

        except:
            conn.rollback()
            print "I am unable to connect to the database"