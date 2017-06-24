#!/usr/bin/python

"""
Created on Thu Mar 30 12:22:59 2017

@author: andrewclawson
"""
import sqlite3 as sql
import CalicoGIS.Analytics.Database as db

class State:
    def __init__(self, name):
        self.Name = name
        self.CountyList = ""


Alabama = State("Alabama");
Alabama.CountyList = ["01005", "01007", "01009", "01011", "01013", "01015", "01017", "01019", "01021", "01023", "01025", "01027", "01029", "01031", "01033", "01035", "01037", "01039", "01041", "01043", "01045", "01047", "01049", "01051", "01053", "01055", "01057", "01059", "01061", "01063", "01065", "01067", "01069", "01071", "01073", "01075", "01077", "01079", "01081", "01083", "01085", "01087", "01089", "01091", "01093", "01095", "01097", "01099", "01101", "01103", "01015", "01107", "01109", "01111", "01113", "01115", "01117", "01119", "01121", "01123", "01125", "01127", "01129", "01131", "01133"]


LOCATIONS_TABLENAME = "locations"
class Location:
    def __init__(self):
        self.PkLocationId = None
        self.FkParentLocationId = None
        self.Name = None
        self.FipsCode = None
        self.FipsCodeInt = None
        self.StateFipsCode = None
        self.CountyFipsCode = None
        self.FipsType = None
        self.StateCode = None
        self.ParentFipsCode = None
        self.State = None
        self.Nation = None
        self.Active = None
    

def GetById(id):
    connection = sql.connect(db.PROCESS_DB)
    cursor = connection.cursor()
    sqlSelect = "SELECT * FROM " + LOCATIONS_TABLENAME + " WHERE pk_location_id = " + str(id)
    print(sqlSelect)
    location = Location()
    for row in cursor.execute(sqlSelect):
        location.PkLocationId = row[0]
        location.FkParentLocationId = row[1]
        location.Name = row[2]
        location.FipsCode = row[3]
        location.FipsCodeInt = row[4]
        location.StateFipsCode = row[5]
        location.CountyFipsCode = row[6]
        location.FipsType = row[7]
        location.StateCode = row[8]
        location.ParentFipsCode = row[9]
        location.State = row[10]
        location.Nation = row[11]
        location.Active = row[12]
    cursor.close()
    connection.close()
    return location
    
def GetByCode(cd):
    connection = sql.connect(db.PROCESS_DB)
    cursor = connection.cursor()
    sqlSelect = "SELECT * FROM " + LOCATIONS_TABLENAME + " WHERE state_cd = '" + cd + "'"
    print(sqlSelect)
    location = Location()
    for row in cursor.execute(sqlSelect):
        location.PkLocationId = row[0]
        location.FkParentLocationId = row[1]
        location.Name = row[2]
        location.FipsCode = row[3]
        location.FipsCodeInt = row[4]
        location.StateFipsCode = row[5]
        location.CountyFipsCode = row[6]
        location.FipsType = row[7]
        location.StateCode = row[8]
        location.ParentFipsCode = row[9]
        location.State = row[10]
        location.Nation = row[11]
        location.Active = row[12]
    cursor.close()
    connection.close()
    return location
        