import xml.etree.ElementTree as etree
from py_osm_package.parsers.tag_parse import *

from shapely.geometry import LinearRing
from shapely.geometry import LineString
from shapely.geometry import Point
from shapely.geometry import Polygon
import shapely.ops
class Relation:
	def __init__(self,osm_tree_child,osm_app):
		print("relation wat")
		self.osm_app =osm_app
		self.id = osm_tree_child.attrib["id"] # id unique in relations
		self.members =parse_members(osm_tree_child)
		self.tags = parse_tags(osm_tree_child) # dictionary of tags, where k= key, v = value
		self.complete=False
		for i in self.members:
			if "type" in i:
				if i["type"]=="way":
					if i["ref"] in osm_app.ways:
						i["object"]=self.osm_app.ways[i["ref"]]
					else:
						self.complete=False
				if i["type"]=="node":
					if i["ref"] in osm_app.nodes:
						i["object"]=self.osm_app.nodes[i["ref"]]
					else:
						self.complete=False
		if self.complete:
			self.geom =None
			if self.tags["type"]=="multipolygon":#this requires special treatment
				self.get_multiploygon()
	
	def get_multiploygon(self):
		outer_ways = []
		inner_ways = []
		for i in members:
			if i["role"]=="inner":
				outer_ways.append(i["object"].geom)
			if i["role"]=="outer":
				inner_ways.append(i["object"].geom)

		inner_polygons =way_list_to_poly_list(inner_ways)
		outer_polygons =way_list_to_poly_list(outer_ways)

		current_pol= inner_polygons[0]
		for i in outer_polygons:
			current_pol = current_pol.union(i)
		outer_pol = current_pol
		self.geom = outer_pol

		if len(inner_polygons)>0:
			current_pol= inner_polygons[0]
			for i in inner_polygons:
				current_pol = inner_polygons.union(i)
			self.geom = outer_pol.difference(current_pol)		
			

	def way_list_to_poly_list(way_list):
		poly_list =[]
		simples = [x for x in way_list if way_list.geom_type=="LinearRing"]
		complexes = [x for x in way_list if way_list.geom_type=="LineString"]
		for i in simples:
			poly_list.append(Polygon(i))
		current_point = list(complexes[0].coords)[0]
		current_list=[]
		complete_complexes=[]
		for i in complexes:
			if list(i[0].coords)[-1] !=current_point:
				current_list.append(i)
			else:
				complete_complexes.append(current_list)
				current_list=[]
		
		for i in complete_complexes:
			res=(shapely.ops.linemerge(i))
			res= LinearRing(res)
			poly_list.append(Polygon(res))

		return poly_list






