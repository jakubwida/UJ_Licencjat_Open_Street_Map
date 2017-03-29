import xml.etree.ElementTree as etree
from py_osm_package.parsers.tag_parse import *
from py_osm_package.osm_app import *
from shapely.geometry import LinearRing
from shapely.geometry import LineString
class Way:
	def __init__(self,osm_tree_child,osm_app):
		#print("way wat")
		self.osm_app =osm_app
		self.id = osm_tree_child.attrib["id"] # id unique in ways
		self.way_nodes=[]
		way_tuples=[]
		self.tags = parse_tags(osm_tree_child) # dictionary of tags, where k= key, v = value
		for i in osm_tree_child:
			if i.tag == "nd":
				node = self.osm_app.nodes[i.attrib["ref"]]
				self.way_nodes.append(node)
				way_tuples.append((node.lat,node.lon))
		self.geom =None
		if self.way_nodes[0]==self.way_nodes[-1]:
			self.geom = LinearRing(way_tuples)
		else:
			self.geom = LineString(way_tuples)			
