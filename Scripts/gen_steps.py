import random as rnd
import numpy as np

def gen_steps(N, p, q, L, Bounds):
	steps = rnd.choices([L,-L], weights = [q*100, p*100], k=N-1)		#Genera N-1 pasos. Direccion -L con probabilidad p y a +L con probabilidad q
	steps = np.insert(steps, 0, 0)			#Agregamos un cero como paso inicial
	X = []							#Vector en el cual se guardaran los pasos acumulados
	X_aux = 0						#Variable auxiliar sobre la cual acumularemos los pasos, es auxiliar porque haremos verificaciones de fronteras


	for i in range(N):
		X_aux += steps[i]
		if Bounds[0] is not None:					#Si existe una frontera superior...
			if X_aux > Bounds[0]: X_aux -= L		#...y si el paso ya la excedio, se resta dicho paso (para mantener el confinamiento)
		if Bounds[1] is not None:					#Si existe una frontera inferior...
			if X_aux < Bounds[1]: X_aux += L 		#...y si el paso ya la excedio, se suma dicho paso (para mantener el confinamiento)
		X.append(X_aux)
	return X