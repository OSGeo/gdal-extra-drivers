#!/usr/bin/env pytest
###############################################################################
# $Id$
#
# Project:  GDAL/OGR Test Suite
# Purpose:  Test IDA format driver.
# Author:   Frank Warmerdam <warmerdam@pobox.com>
#
###############################################################################
# Copyright (c) 2005, Frank Warmerdam <warmerdam@pobox.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

from osgeo import gdal


import gdaltest
import pytest

###############################################################################
# Perform simple read test.


def test_ida_1():

    tst = gdaltest.GDALTest('ida', 'ida/DWI01012.AFC', 1, 4026)
    return tst.testOpen()

###############################################################################
# Verify some auxiliary data.


def test_ida_2():

    ds = gdal.Open('data/ida/DWI01012.AFC')

    gt = ds.GetGeoTransform()

    if gt[0] != -17.875 or gt[1] != 0.25 or gt[2] != 0 \
       or gt[3] != 37.875 or gt[4] != 0 or gt[5] != -0.25:
        print('got: ', gt)
        pytest.fail('Aaigrid geotransform wrong.')

    prj = ds.GetProjection()
    assert 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]', \
        ('Projection does not match expected:\n%s' % prj)

    band1 = ds.GetRasterBand(1)
    assert band1.GetNoDataValue() == 255, 'Grid NODATA value wrong or missing.'

    assert band1.DataType == gdal.GDT_Byte, 'Data type is not byte.'

###############################################################################
# Create simple copy and check.


def test_ida_3():

    tst = gdaltest.GDALTest('ida', 'ida/DWI01012.AFC', 1, 4026)

    prj = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9108"]],AXIS["Lat",NORTH],AXIS["Long",EAST],AUTHORITY["EPSG","4326"]]'

    return tst.testCreateCopy(check_gt=0, check_srs=prj, check_minmax=1)

###############################################################################
# Test ACEA Projection.


def test_ida_4():

    gdaltest.ida_tst = gdaltest.GDALTest('ida', 'ida/DWI01012.AFC', 1, 4026)

    prj = """PROJCS["unnamed",
    GEOGCS["Clarke 1866",
        DATUM["Clarke 1866",
            SPHEROID["Clarke 1866",6378206.4,293.9786982138966]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433]],
    PROJECTION["Albers_Conic_Equal_Area"],
    PARAMETER["standard_parallel_1",10],
    PARAMETER["standard_parallel_2",25],
    PARAMETER["latitude_of_center",17.5],
    PARAMETER["longitude_of_center",-87.5],
    PARAMETER["false_easting",0],
    PARAMETER["false_northing",0],
    UNIT["meter",1]]"""

    return gdaltest.ida_tst.testSetProjection(prj=prj)

###############################################################################
# Test Goodes Projection.


def test_ida_5():

    gdaltest.ida_tst = gdaltest.GDALTest('ida', 'ida/DWI01012.AFC', 1, 4026)

    prj = """PROJCS["unnamed",
    GEOGCS["Sphere",
        DATUM["Sphere",
            SPHEROID["Sphere",6370997,0]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433]],
    PROJECTION["Goode_Homolosine"],
    PARAMETER["central_meridian",0],
    PARAMETER["false_easting",0],
    PARAMETER["false_northing",0],
    UNIT["meter",1],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH]]"""

    return gdaltest.ida_tst.testSetProjection(prj=prj)

###############################################################################
# Test LCC Projection.


def test_ida_6():

    gdaltest.ida_tst = gdaltest.GDALTest('ida', 'ida/DWI01012.AFC', 1, 4026)

    prj = """PROJCS["unnamed",
    GEOGCS["Clarke 1866",
        DATUM["Clarke 1866",
            SPHEROID["Clarke 1866",6378206.4,293.9786982138966]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433]],
    PROJECTION["Lambert_Conformal_Conic_2SP"],
    PARAMETER["standard_parallel_1",33.90363402775256],
    PARAMETER["standard_parallel_2",33.62529002776137],
    PARAMETER["latitude_of_origin",33.76446202775696],
    PARAMETER["central_meridian",-117.4745428888127],
    PARAMETER["false_easting",0],
    PARAMETER["false_northing",0],
    UNIT["meter",1]]"""

    return gdaltest.ida_tst.testSetProjection(prj=prj)

###############################################################################
# Test LAEA Projection.


def test_ida_7():

    gdaltest.ida_tst = gdaltest.GDALTest('ida', 'ida/DWI01012.AFC', 1, 4026)

    prj = """PROJCS["unnamed",
    GEOGCS["Sphere",
        DATUM["Sphere",
            SPHEROID["Sphere",6370997,0]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433]],
    PROJECTION["Lambert_Azimuthal_Equal_Area"],
    PARAMETER["latitude_of_center",33.76446202775696],
    PARAMETER["longitude_of_center",-117.4745428888127],
    PARAMETER["false_easting",0],
    PARAMETER["false_northing",0],
    UNIT["meter",1]]"""

    return gdaltest.ida_tst.testSetProjection(prj=prj)




