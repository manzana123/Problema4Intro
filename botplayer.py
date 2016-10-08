import numpy
import random

def calcularCuadrante(cuadrante, mayorAmen = 0):
	if cuadrante == 0:
		if mayorAmen <= 1:
			return "2,0"
		elif mayorAmen == 2:
			return "1,0"
		elif mayorAmen == 3:
			return "3,0"		
	elif cuadrante == 1:
		if mayorAmen <= 1:
			return "0,2"
		elif mayorAmen == 2:
			return "0,1"
		elif mayorAmen == 3:
			return "0,3"
	elif cuadrante == 2:
		if mayorAmen <= 1:
			return "-2,0"
		elif mayorAmen == 2:
			return "-1,0"
		elif mayorAmen == 3:
			return "-3,0"
	elif cuadrante == 3:
		if mayorAmen <= 1:
				return "0,-2"
		elif mayorAmen == 2:
			return "0,-1"
		elif mayorAmen == 3:
			return "0,-3"
	return "0,-2"

def escoger_movimiento( amenazas ):
	#movimiento_y = ""
	#movimiento_x = ""
	mayorCuad = -1
	mayorAmen = 0
	gradoMayor = 0
	amenDirecta = dict()
	amenazas = amenazas.strip().split(':')
	if len(amenazas) == 1:
		AmenCuad = amenazas[0].split('-')
		for i in range(4):
			if mayorCuad < AmenCuad[i]:
				mayorCuad = AmenCuad[i]
				cuadLoc = i				
	elif len(amenazas) == 2:
		AmenCuad = amenazas[1].split('-')
		for i in range(4):
			if mayorCuad < AmenCuad[i]:
				mayorCuad = AmenCuad[i]
				cuadLoc = i
		AmenDir = amenazas[0].split('-')
		for i in range(len(AmenDir)):
			if str(i) in "123":
				if i not in amenDirecta:
					amenDirecta[i] = 0
				amenDirecta[i] += 1
	for i in amenDirecta:
		if amenDirecta[i] > mayorAmen:
			mayorAmen = amenDirecta[i]
			gradoMayor = i
	print amenDirecta
	print mayorCuad
	if len(amenDirecta) == 0:
		hueaita = calcularCuadrante(mayorCuad, 0)
	hueaita = calcularCuadrante(mayorCuad,gradoMayor)
	return hueaita
					
def escoger_disparo( amenazas ):
	#disparo_x = ""
	#disparo_y = ""
	amenazas = amenazas.strip().split(':')
	a = random.randint(1,2)
	if a%2 == 0:
		return str(random.randint(-5,5))+",0"
	else:
		return "0,"+str(random.randint(-5,5))
	#return disparo_x + "," + disparo_y
