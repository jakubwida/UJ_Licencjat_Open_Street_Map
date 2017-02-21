from py_osm_package.osm_parser import *
from py_osm_package.data_visualisation import *
from py_osm_package.data_format import *

parser = OSMParser()
data_object = parser.default_parse("map(1).osm")
visu =Visualisation()
visu.default_draw(data_object)