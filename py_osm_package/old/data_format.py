


class DataFormat:
	""""class intended for storing simple set of points and their description"""
	def __init__(self,description):
		"""creates empty data format, requires description, a [string,string...] list of what consecutive fields in list row (field,field ...) stand for. EX: description ["x","y"] gives away that list will look like this: [(1.0,2.0),(2.0,3.0),(1.0,2.0),(1.4,1.2)...] as each list element is tuple with field1 ="x" and field 2 ="y" """
		self.points=[]
		self.description = description
	
	def add_point(self,value):
		"""adds another tuple (value) to the list"""
		self.points.append(value)
		
