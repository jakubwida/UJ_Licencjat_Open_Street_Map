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
	


