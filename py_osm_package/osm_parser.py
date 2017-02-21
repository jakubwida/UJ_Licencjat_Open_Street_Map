import xml.etree.ElementTree as etree
from py_osm_package.data_format import *

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
					if(i.attrib['k']=='addr:city'):
						out_data.add_point((child.attrib['lon'],child.attrib['lat'],1.0))
						print(child.attrib['lat'],child.attrib['lon'])

		return out_data
