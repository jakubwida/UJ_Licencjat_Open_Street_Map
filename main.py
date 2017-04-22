from py_osm_package.parsers.parser import Parser
from py_osm_package.visualisation.visu import *

from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import math


obj = Parser("map.osm")


data = []
for i in list(obj.ways.values()):
	if "building" in i.tags:
		data.append(list(i.geom.centroid.coords)[0])


from py_osm_package.cluster.scikit import scikit_affinite_propagation
out_data=scikit_affinite_propagation(data)
draw_clusters(out_data)

for i in list(obj.relations.values()):
	draw_sympy(i.geom,"r-")
	#if "building" in i.tags:
	#	draw_sympy(i.geom,"r-")
for i in list(obj.ways.values()):
	if "building" in i.tags:
		draw_sympy(i.geom,"g-")
plt.show()
