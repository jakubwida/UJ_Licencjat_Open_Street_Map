import matplotlib.pyplot as plt

def draw_sympy(figure,decoration_string):
	if figure!=None:
		if figure.geom_type=="Polygon":
			draw_sympy(figure.exterior,decoration_string)
			for i in figure.interiors:
				draw_sympy(i,decoration_string)
		elif figure.geom_type=="MultiPolygon":
			for i in figure:
				draw_sympy(i,decoration_string)
		elif figure.geom_type=="GeometryCollection":
			for i in figure:
				draw_sympy(i,decoration_string)
		else:
			lis=list(zip(*list(figure.coords)))
			plt.plot(lis[0],lis[1],decoration_string)

""" draws [((x1,y1),(x2,y2),(x3,y3), ...),(...)] array of clusters. each ((x,y)...) array
describes single cluster, so array of them is array of all clusters. it possible significance added later"""
def draw_clusters(data_list):

	prop_cycle = plt.rcParams['axes.prop_cycle']
	colors = prop_cycle.by_key()['color']
	clen=len(colors)

	for index,i in enumerate(data_list):
		twolists=list(zip(*i))
		color = colors[index%clen]
		plt.plot(twolists[0],twolists[1],'o',color=color)


#needs to be tested
