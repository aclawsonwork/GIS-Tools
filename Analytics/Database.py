# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import sys
import os
import sqlite3
import time
import datetime
import CalicoGIS.Path as path

PROCESS_DB = path.DATABASE_BASE_PATH + "/processes.db"

class DBWriter:
    def __init__(self, process):
        self.Process = process
        self.Tablename = process.Tablename
        self.InsertStatement = None
        self.Connection = None
        self.Cursor = None
        
    def BuildInsertStatement(self):
        dateString = str(self.Process.Date.year) + "-"+ str(self.Process.Date.month) + "-" + str(self.Process.Date.day)
        #elapsedTime = process.ElapsedTime
        
        insertSQL = "INSERT INTO " + PROCESS_DB + "." + self.Tablename + " (date, elapsed_time) "
        insertSQL = insertSQL + "VALUES(" + dateString + ", " + str(self.Process.ElapsedTime) + ")"
        self.InsertStatement = insertSQL
        
        # logic for adding to sqlite db
    def Write(self):
        self.BuildInsertStatement()
        self.Connection = sqlite3.connect(PROCESS_DB)
        self.Cursor = self.Connection.cursor()
        self.Cursor.execute(self.InsertStatement)
        self.Cursor.close()
        
    
    
        
        
class Process:
    
    def __init__(self):
        self.Writer = None
        self.Tablename = None
        self.Date = datetime.date.today()
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.ElapsedTime = None
    
    def Start(self):
        self.StartTime = time.time()
        
    def Stop(self):
        self.EndTime = time.time()
        self.ElapsedTime = self.EndTime - self.StartTime
        #self.Writer.Write()
            
class StateBoundaryExtract(Process):
    def __init__(self):
        self.Name = "State Boundary Extract"
        self.Tablename = "state_boundary_extract"
        self.Date = datetime.date.today()
        self.Writer = DBWriter(self)
        
    
        
        
            
            
        
            
        
        