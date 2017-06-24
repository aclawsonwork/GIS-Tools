# -*- coding: utf-8 -*-
import sys
import os
import sqlite3
import time
import datetime
import CalicoGIS.Path as path
import CalicoGIS.Analytics.Database as db
import CalicoGIS.Locations as loc

STATE_IMPORT_TYPE = 1
STATE_BOUNDARY_EXTRACT_TYPE = 2
RASTER_EXTRACT_TYPE = 3
CONVERT_RASTOR_TO_POLYGON_TYPE = 4
IMPORT_TO_SDE_TYPE = 5

class Process:
    
    def __init__(self):
        self.Writer = None
        self.Location = None
        self.Date = datetime.date.today()
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.ElapsedTime = None
    
    def SetLocation(self, locationCode):
        self.Location = loc.GetByCode(locationCode)
    
    def Start(self):
        self.StartTime = time.time()
        
    def Stop(self):
        self.EndTime = time.time()
        self.ElapsedTime = self.EndTime - self.StartTime
        #self.Writer.Write()
    def Write(self):
        self.Writer.Write()

class StateImportProcess(Process):
    def __init__(self):
        self.Name = "State Import Process"
        self.ProcessTypeId = STATE_IMPORT_TYPE
        self.Date = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class StateBoundaryExtract(Process):
    def __init__(self):
        self.Name = "State Boundary Extract"
        
        self.ProcessTypeId = STATE_BOUNDARY_EXTRACT_TYPE
        self.Date = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class ExtractByMask(Process):
    def __init__(self):
        self.Name = "Extract Raster By Mask"
        self.ProcessTypeId = RASTER_EXTRACT_TYPE
        self.Date = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class ConvertRasterToPolygon(Process):
    def __init__(self):
        self.Name = "Convert Raster to Polygon"
        self.ProcessTypeId = CONVERT_RASTOR_TO_POLYGON_TYPE
        self.Date = datetime.date.today()
        self.Writer = db.DBWriter(self)
        
class ImportPolygonToSDE(Process):
    def __init__(self):
        self.Name = "Import Polygon To SDE"
        self.ProcessTypeId = IMPORT_TO_SDE_TYPE
        self.Date = datetime.date.today()
        self.Writer = db.DBWriter(self)