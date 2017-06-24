# -*- coding: utf-8 -*-
import sys
import os
import sqlite3
import time
import datetime
import CalicoGIS.Path as path
import CalicoGIS.Analytics.Database as db

STATE_IMPORT_TYPE = 1
STATE_BOUNDARY_EXTRACT_TYPE = 2
RASTER_EXTRACT_TYPE = 3
CONVERT_RASTOR_TO_POLYGON_TYPE = 4
IMPORT_TO_SDE = 5

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
    def Write(self):
        self.Writer.Write()
            
class StateBoundaryExtract(Process):
    def __init__(self):
        self.Name = "State Boundary Extract"
        self.Tablename = "state_boundary_extract"
        self.Date = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class ExtractByMask(Process):
    def __init__(self):
        self.Name = "Extract Raster By Mask"
        self.Tablename = "raster_extract"
        self.Data = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class ConvertRasterToPolygon(Process):
    def __init__(self):
        self.Name = "Convert Raster to Polygon"
        self.Tablename = "raster_conversion"
        self.Data = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class ImportPolygonToSDE(Process):
    def __init__(self):
        self.Name = "Import Polygon To SDE"
        self.Tablename = "import_polygon"
        self.Data = datetime.date.today()
        self.Writer = db.DBWriter(self)