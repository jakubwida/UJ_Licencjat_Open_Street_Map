from py_osm_package.parsers.node import *
from py_osm_package.parsers.way import *
from py_osm_package.parsers.relation import *
from py_osm_package.visualisation.visu import *

from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import math



import xml.etree.ElementTree as etree
class OSMApp:
	def __init__(self,filename):
		self.nodes = {} #{id:node}
		self.ways = {} # {id:way}
		self.relations ={} # {id:relation}

		tree = etree.parse(filename)
		root = tree.getroot()

		for child in root:
			tag = child.tag
			if tag =="node":
				self.nodes[child.attrib["id"]]=Node(child)
			elif tag =="way":
				self.ways[child.attrib["id"]]=Way(child,self)
			elif tag =="relation":
				self.relations[child.attrib["id"]]=Relation(child,self)

		for i in list(self.ways.values()):
			draw_sympy(i.geom,"r-")
			#if "building" in i.tags:
			#	draw_sympy(i.geom,"r-")
		plt.show()

"""

		fig = plt.figure()
		ax = fig.add_subplot(111)

		for key in self.ways: 
			ax.add_patch(PathPatch(self.ways[key].matplotlib_path, facecolor='none', lw=2))
			print(PathPatch(self.ways[key].matplotlib_path))

		ax.set_xlim(50.1,50.2)
		ax.set_ylim(19.95,20.05)
		plt.show()
"""
