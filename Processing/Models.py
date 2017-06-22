# -*- coding: utf-8 -*-

import arcpy
from arcpy import env
from arcpy.sa import * 

import GopherGIS.Locations as loc
import GopherGIS.Path as path



class StateCropRasterBuilder:
    
    
    def __init__(self, stateAbbreviation, rasterTitle):
        self.StateAbbreviation = stateAbbreviation
        self.RasterTitle = rasterTitle
        self.StateBoundaryPath = path.STATE_BOUNDARY_TIGER_PATH + self.StateAbbreviation
        self.CropRasterOutputPath = path.CROP_RASTER_BASE_PATH + rasterTitle + self.StateAbbreviation
        self.CropPolygonOutputPath = path.CROP_POLYGON_BASE_PATH + self.RasterTitle + "_" + self.StateAbbreviation
        
    def ExportStateBoundaries(self):
        message = "Extracting state boundary for: " + self.StateAbbreviation
        print(message)
        arcpy.Select_analysis(
                              in_features = path.STATE_BOUNDARY_INPUT,
                              out_feature_class = self.StateBoundaryPath,
                              where_clause = "STUSPS = '" + self.StateAbbreviation + "'"
                              )
        
        message = "State boundary extraction succeeded."
        print(message)
        
    def ExtractCropRasterFromStateMask(self, imageName):
        message = "Extracting crop raster from state mask for " + self.StateAbbreviation
        print(message)
        
        inputDir = path.CROP_RASTER_BASE_PATH + self.RasterTitle
        self.CropRasterOutputPath = path.CROP_RASTER_BASE_PATH + self.RasterTitle + "_" + self.StateAbbreviation
        outExtractByMask = ExtractByMask(inputDir, self.StateBoundaryPath)
        outExtractByMask.save(self.CropRasterOutputPath)
        
        message = "Finished extracting state crop raster for " + self.StateAbbreviation
        
    def ConvertCropRasterToPolygon(self):
        message = "Converting crop rastoer for " + self.StateAbbreviation + " to polygon"
        print(message)
        
        arcpy.RasterToPolygon_conversion(
                                         in_raster = self.CropRasterOutputPath,
                                         out_polygon_features = self.CropPolygonOutputPath,
                                         simplify = "NO_SIMPLIFY",
                                         raster_field = "VALUE"
                                         )
        
        message = "Finished converting crop raster to polygon for " + self.StateAbbreviation
        print(message)
        
        
