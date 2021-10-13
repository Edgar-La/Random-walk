import matplotlib.pyplot as plt

def plotter(X, Bounds, dcm):
	fig = plt.figure(figsize = (14,5))


	ax1 = fig.add_subplot(1,2,1)
	ax1.plot(X)																					#Graficamos el vector que contiene los pasos acumulados
	if Bounds[0] is not None: ax1.axhline(y=Bounds[0], color = 'r', linestyle ='--')			#Grafica frontera superior (si la hay)
	if Bounds[1] is not None: ax1.axhline(y=Bounds[1], color = 'r', linestyle ='--')			#Grafica frontera inferior (si la hay)
	ax1.set_title('Random Walker'); ax1.set(xlabel='Time (t)', ylabel='Position (x)')			#Agrega titulo y nombre de etiquetas al grafico 1

	ax2 = fig.add_subplot(1,2,2)
	ax2.plot(dcm)																				#Graficamos el vector que contiene los datos del dcm
	ax2.set_title('DCM'); ax2.set(xlabel='', ylabel='')											#Agrega titulo y nombre de etiquetas al grafico 2

	
	
	plt.show()																					#Mostramos el grafico compuesto
