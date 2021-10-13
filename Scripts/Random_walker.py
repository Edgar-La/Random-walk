import os; os.system('clear')					#Limpiamos la terminal

from gen_steps import gen_steps					#Del script gen_steps.py importamos la funcion gen_steps
from DCM import DCM								#Del script DCM.py importamos la funcion DCM
from plotter import plotter						#Del script plotter.py importamos la funcion plotter





#Parametros que el usuario puede modificar
#########################################################################################################################################################
#########################################################################################################################################################

N = 100							#Cantidad de pasos
L = 1 							#Tamaño de paso
p = .5							#Probabilidad p de obtener un paso +L
q = 1 - p						#Probabilidad q de obtener un paso -L (esta no se modifica, ya que basta con ajustar el valor de p)
Bounds = [None, None]			#Las fronteras deben ser de tipo int para asignar un valor, o None para omitir dicha frontera. Puede ser sola una o ambas
								#Ejemplos: Bounds = [20, -20], Bounds = [None, -20], Bounds = [20, None]
#########################################################################################################################################################
#########################################################################################################################################################






#Esta seccion llama a los respectivas funciones que se importaron al inicio
X = gen_steps(N, p, q, L, Bounds)		#Funcion que genera los pasos con los paramétros elegidos
dcm = DCM(X)							#Funcion que calcula el desplazamiento cuadratico medio
plotter(X, Bounds, dcm)					#Funcion que grafica los pasos y el desplazamiento
