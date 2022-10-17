import pandas as pd
import csv
import geopandas as gpd
import fiona
import os

ParentPath = "/Scripts"
gdbPath = ".../HF3x7_1999to2017_public.gdb"

# Get the list of all feature types associated with wells. We will use all of them as we don't know what type the sampling sites are in.

exampleLayer = gpd.read_file(gdbPath, driver='FileGDB', layer='HF_3x7_2015')
featureList = exampleLayer.FEATURE_TY.unique()
WellTypesList = []
for i in featureList:
    if 'WELL' in i:
        WellTypesList.append(i)
os.chdir(ParentPath)
with open('Data/Processed/list_of_well_features.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(WellTypesList)

def extract_well_polygons(multilayerd_gdb):
    list_of_gdf = []
    number_of_rows = []
    for name in fiona.listlayers(multilayerd_gdb):
        # All the layers are YEAR, except for one random other layer
        if name != "ll_lisXharvest2017":
            print(name)
            layer = gpd.read_file(multilayerd_gdb, driver='FileGDB', layer=name)
            layer = layer.loc[layer['FEATURE_TY'].isin(WellTypesList)]
            # add a column with the year
            layer['YEAR'] = name[-4:]

            list_of_gdf.append(layer)
            print("appended")
            # print("number of columns in single layer: " + layer.shape[1])
            size = len(layer)
            number_of_rows.append(size)
            print(size)
    print("Number of rows expected: " + str(sum(number_of_rows)))
    concatenated_gdb = gpd.GeoDataFrame(pd.concat(list_of_gdf, ignore_index=True), crs=list_of_gdf[0].crs)
    print("made the concat gdb")
    print("Number of rows in concatenated gdb: " + str(len(concatenated_gdb)))

    # print("number of columns in single layer: " + concatenated_gdb.shape[1])
    os.chdir(r"C:\Users\ilebe\OneDrive\Documents\!Masters!\Harvests v Wells")

    concatenated_gdb.to_file("Data/Processed/wellsites_by_year.shp")
    return
extract_well_polygons(gdbPath)