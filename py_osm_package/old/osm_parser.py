import xml.etree.ElementTree as etree
from py_osm_package.parsers.data_format import *


#old, do not use 

class OSMParser:
	"""class created for parsing osm files with various options"""
	def __init__(self): pass

	def default_parse(self,filename):
		"""parses osm file given its name into data_format.DataFormat with lat,lon,val as description"""
		out_data= DataFormat(["lat","lon","val"])

		tree = etree.parse(filename)
		root = tree.getroot()

		for child in root:
			tags = child
			for i in tags:
				if 'k' in i.attrib:
					if(i.attrib['k']=='addr:city' and "lat" in child.attrib and "lon" in child.attrib):
						out_data.add_point((child.attrib['lon'],child.attrib['lat'],1.0))
						print(child.attrib['lat'],child.attrib['lon'])

		return out_data



	def unadressed_parse(self,filename):
		"""parses osm file given its name into data_format.DataFormat with lat,lon,val as description, parsing building objects rather than address nodes"""
		out_data= DataFormat(["lat","lon","val"])

		tree = etree.parse(filename)
		root = tree.getroot()
		list_of_buildings=[]


		for child in root:
			for i in child:
				if 'k' in i.attrib:
					if(i.attrib['k']=='building'):
						list_of_buildings.append(child[0].attrib['ref'])
						#print(child[0].attrib['ref'])
		for child in root:
			if "id" in child.attrib:
				for i in list_of_buildings:
					if child.attrib["id"]==str(i):
						out_data.add_point((child.attrib['lon'],child.attrib['lat'],1.0))

		return out_data
