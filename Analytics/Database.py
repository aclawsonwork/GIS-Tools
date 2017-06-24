# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import sys
import os
import sqlite3
import time
import datetime
import CalicoGIS.Path as path

PROCESS_DB = path.DATABASE_BASE_PATH + "/processes.db"
PROCESS_TABLE = "process"

class DBWriter:
    def __init__(self, process):
        self.Process = process
        self.Tablename = process.Tablename
        self.InsertStatement = None
        self.InsertValues = None
        self.Connection = None
        self.Cursor = None
        
    def BuildInsertStatement(self):
        dateString = str(self.Process.Date.year) + "-"+ str(self.Process.Date.month) + "-" + str(self.Process.Date.day)
        #elapsedTime = process.ElapsedTime
        
        insertSQL = "INSERT INTO " + PROCESS_TABLE + " (fk_process_type_id, fk_location_id, process_date, elapsed_time_seconds) VALUES(?,?,?,?)"
        self.InsertValues = (self.Process.ProcessTypeId, self.Process.Location.PkLocationId, dateString, str(self.Process.ElapsedTime))
        self.InsertStatement = insertSQL
        
        # logic for adding to sqlite db
    def Write(self):
        self.BuildInsertStatement()
        self.Connection = sqlite3.connect(PROCESS_DB)
        self.Cursor = self.Connection.cursor()
        self.Cursor.execute(self.InsertStatement,self.InsertValues)
        self.Connection.commit()
        self.Cursor.close()
        self.Connection.close()


        
    
        
        
            
            
        
            
        
        