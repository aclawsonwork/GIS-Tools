# -*- coding: utf-8 -*-
'''
A script to manage each of the paths necessary for the GIS preprocessing.
'''
import os



# - App dirctoriess
MODULE_NAME = "/GopherGIS"

APP_PATH = os.getcwd()
DATABASE_BASE_PATH = APP_PATH[:-len(MODULE_NAME)] + "/Databases"


# - Raster / Polygon IO dircetories
PREPROCESSING_TEMP_DIR = "D:/Projects/CSI_FESTF/GIS/Processing_Data/Temp/"
TEMP_VECTOR_FOLDER = "Preprocessing_Temp_Vector.gdb/"
TEMP_RASTER_FOLDER = "Preprocessing_Temp_Raster.gdb/"


TIGER_PROJECTION_PREFIX = "rf_us_na_pr_vi_bndry_tiger_"
STATE_BOUNDARY_TIGER_PATH = PREPROCESSING_TEMP_DIR + TEMP_VECTOR_FOLDER + TIGER_PROJECTION_PREFIX
#STATE_BOUNDARY_TIGER_PROJECTION = "D:/Projects/CSI_FESTF/GIS/geodatabases/Preprocessing_Temp_Files.gdb/rf_us_na_pr_vi_bndry_tiger" # Taken from line 29
CROP_POLYGON_BASE_PATH = PREPROCESSING_TEMP_DIR + TEMP_VECTOR_FOLDER

CROP_RASTER_BASE_PATH = PREPROCESSING_TEMP_DIR + TEMP_RASTER_FOLDER

STATE_BOUNDARY_INPUT = "D:/Projects/CSI_FESTF/GIS/Processing_Data/Temp/Preprocessing_Temp_Vector.gdb/rf_us_na_pr_vi_bndry_prj"

