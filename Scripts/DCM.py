import numpy as np
def DCM(X):
	dcm = []
	v_aux= []
	for Dt in range(1, len(X)):							#Ciclo el cual va a incrementar Delta t
		v_aux.clear()									#Cada que usemos un valor diferente de Delta t se limpia el vector auxiliar
		for i in range(len(X)):							#Ciclo para desplazarnos sobre las posiciones X
			if (i+Dt) < len(X):							#Verificamos que i y Delta siguen siendo menores a N
				v_aux.append((X[i+Dt]-X[i])**2)			#Vamos agregando en el vector auxiliar
			else:
				break
		dcm.append(np.mean(v_aux))						#Calculamos el promedio del vector auxiliar y repetimos lo anterior para el siguiente Delta t
	return dcm