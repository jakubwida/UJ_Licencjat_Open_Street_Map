import matplotlib.pyplot as plt
import math
#from data_format import *

class Visualisation:
	""" class drawing DataFormat objects, with given options """
	def __init__(self): pass
	def default_draw(self,data_format):
		""" default representation of default parsed osm file: description lat,lon,value -> x, y, size of point"""
		plt.ylabel("lat")
		plt.xlabel("lon")
		for i in data_format.points:
			plt.plot(i[0], i[1], 'ro',ms=i[2])
		plt.show()
	

