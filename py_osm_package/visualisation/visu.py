import matplotlib.pyplot as plt

def draw_sympy(figure,decoration_string):
	lis=list(zip(*list(figure.coords)))
	plt.plot(lis[0],lis[1],decoration_string)

