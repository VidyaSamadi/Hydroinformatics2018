###Jupyter notebooks ######

import arcgis
from arcgis.gis import GIS
from IPython.display import display
        
import getpass
from arcgis.gis import *

user_name = 'username'
password = getpass.getpass("Please enter password: ")
dev_gis = GIS('https://www.arcgis.com', 'username', password)
print("Successfully logged in to {} as {}".format(dev_gis.properties.urlKey + '.' + dev_gis.properties.customBaseUrl,
                                                 dev_gis.users.me.username))
ago_gis = GIS()
gis = GIS("https://www.arcgis.com", "username", "password")

from arcgis.gis import GIS

user_name = 'username'
password = 'password'
my_gis = GIS('https://www.arcgis.com', user_name, password)

map = gis.map("imagery")
map

from arcgis.gis import GIS

gis = GIS()
map = gis.map('Streets,SC', 6)
map

import datetime
import arcgis
from arcgis.gis import GIS
from IPython.display import display
import pandas as pd

# create a Web GIS object
gis = GIS("https://python.playground.esri.com/portal", "username", "password")
from math import sqrt

map = gis.map("imagery")
map

import numpy as np
np.sqrt

import ipywidgets
print(ipywidgets.__version__)

conda create -n newenvname python=3.6
activate newenvname
conda install -c esri arcgis
 
import widgetsnbextension
import ipywidgets
import arcgis

print(widgetsnbextension.__version__)
print(ipywidgets.__version__)
print(arcgis.__version__)
