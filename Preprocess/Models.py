# -*- coding: utf-8 -*-

import arcpy
#from arcpy import env
#from arcpy.sa import * 
import CalicoGIS.Path as path
import CalicoGIS.Analytics.Database as db
import CalicoGIS.Analytics.Process as proc



class StateCropRasterBuilder:
    
    
    def __init__(self, stateAbbreviation, rasterTitle):
        self.StateAbbreviation = stateAbbreviation
        self.RasterTitle = rasterTitle
        self.StateBoundaryPath = path.STATE_BOUNDARY_TIGER_PATH + self.StateAbbreviation
        self.CropRasterOutputPath = path.CROP_RASTER_BASE_PATH + rasterTitle + self.StateAbbreviation
        self.CropPolygonOutputPath = path.CROP_POLYGON_BASE_PATH + self.RasterTitle + "_" + self.StateAbbreviation
        
    def ExportStateBoundaries(self):
        process = proc.StateBoundaryExtract()
        message = "Extracting state boundary for: " + self.StateAbbreviation
        print(message)
        process.Start()
        arcpy.Select_analysis(
                              in_features = path.STATE_BOUNDARY_INPUT,
                              out_feature_class = self.StateBoundaryPath,
                              where_clause = "STUSPS = '" + self.StateAbbreviation + "'"
                              )
        process.Stop()
        message = "State boundary extraction succeeded." 
        print(message)
        message = "Process Time: " + str(process.ElapsedTime) + " seconds"
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
        message = "Converting crop raster for " + self.StateAbbreviation + " to polygon"
        print(message)
        
        arcpy.RasterToPolygon_conversion(
                                         in_raster = self.CropRasterOutputPath,
                                         out_polygon_features = self.CropPolygonOutputPath,
                                         simplify = "NO_SIMPLIFY",
                                         raster_field = "VALUE"
                                         )
        
        message = "Finished converting crop raster to polygon for " + self.StateAbbreviation
        print(message)
        
        
