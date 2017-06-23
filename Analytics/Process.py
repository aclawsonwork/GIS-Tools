# -*- coding: utf-8 -*-
import sys
import os
import sqlite3
import time
import datetime
import CalicoGIS.Path as path
import CalicoGIS.Analytics.Database as db

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
        self.Writer = db.DBWriter(self)