
The geodatabase structure of the Human Footprint Inventory is as a multilayer gdb, separated by year. In each layer, the sublayers for each human disturbance are merged in one geo table.

While if we know the disturbance type in which our study site is located, we don't know the year of the distrubance. To check which polygon your site coordinates fall into, we would have to check for every yeared layer. Loading and geospatially joining two geodatabases is computationally lengthy; a better way would be to extract the desired disturbance polygons from each year, append a 'year' column matching the layer, and vertically merge the extracted polygons into one "chosen disturbance" polygons layer from 1999-2017.


ABMI Human Footprint geodatabase: https://www.abmi.ca/home/data-analytics/da-top/da-product-overview/Human-Footprint-Products/Human-Footprint-Sample-Based-Inventory.html?scroll=true

+ Metadata: https://ftp-public.abmi.ca/GISData/HumanFootprint/2019/HFI2019_Metadata_v2.pdf