from py_osm_package.parsers.node import *
from py_osm_package.parsers.way import *
from py_osm_package.parsers.relation import *
import xml.etree.ElementTree as etree

class Parser:
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
