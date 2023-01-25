from pyrsgis import raster
from osgeo import gdal 
import os 
import glob
import rasterio
import numpy as np
import matplotlib.pyplot as plt

def scaleMinMax(x):
    return((x - np.nanmin(x))/(np.nanmax(x) - np.nanmin(x)))

Band1 = gdal.Open('Images\LC08_L2SP_001073_20150511_20200909_02_T1_SR_B2.TIF')
b = Band1.ReadAsArray()
Band2 = gdal.Open('Images\LC08_L2SP_001073_20150511_20200909_02_T1_SR_B3.TIF')
g = Band2.ReadAsArray()
Band3 = gdal.Open('Images\LC08_L2SP_001073_20150511_20200909_02_T1_SR_B4.TIF')
r = Band3.ReadAsArray()

r = scaleMinMax(r)
g = scaleMinMax(g)
b = scaleMinMax(b)

rgb = np.dstack((r,g,b))


#rgbMin = rgb.min()
#rgbMax = rgb.max()
#rgbMean = (rgbMin + rgbMax)/2

#print (rgbMax)

#Image = np.where((rgb< rgbMean), 50000000, rgb)


driver = gdal.GetDriverByName("GTiff")
outds = driver.Create("Output.TIF", 7771, 7651, 3, gdal.GDT_UInt16)
for i in range(3):
    outband = outds.GetRasterBand(i+1)
    outband.WriteArray(rgb[i])

outband = None
outds = None

#Reproject = gdal.Warp("reproject.tif", rgb, dstSRS = "EPSG: 4326")


