import numpy
import random

def calcularCuadrante(cuadrante, mayorAmen = 0):
	print cuadrante, mayorAmen
	if cuadrante == 0:
		if mayorAmen == 1 or mayorAmen == 0:
			return "2,0"
		elif mayorAmen == 2:
			return "1,0"
		elif mayorAmen == 3:
			return "3,0"		
	elif cuadrante == 1:
		if mayorAmen == 1 or mayorAmen == 0:
			return "0,2"
		elif mayorAmen == 2:
			return "0,1"
		elif mayorAmen == 3:
			return "0,3"
	elif cuadrante == 2:
		if mayorAmen == 1 or mayorAmen == 0:
			return "-2,0"
		elif mayorAmen == 2:
			return "-1,0"
		elif mayorAmen == 3:
			return "-3,0"
	elif cuadrante == 3:
		if mayorAmen == 1 or mayorAmen == 0:
				return "0,-2"
		elif mayorAmen == 2:
			return "0,-1"
		elif mayorAmen == 3:
			return "0,-3"
	else:
		return "-2,0"

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
		for i in range(len(AmenCuad)):
			if mayorCuad < AmenCuad[i]:
				mayorCuad = AmenCuad[i]
				cuadLoc = i				
	elif len(amenazas) == 2:
		AmenCuad = amenazas[1].split('-')
		for i in range(len(AmenCuad)):
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
	if mayorCuad != None:
		if len(amenDirecta) == 0:
			return calcularCuadrante(cuadLoc, 0)
		else:
			return calcularCuadrante(cuadLoc,gradoMayor)
	else:
		return "0,1"
					
def escoger_disparo( amenazas ):
	#disparo_x = ""
	#disparo_y = ""
	amenazas = amenazas.strip().split(':')
	a = random.randint(1,2)
	disparo = 0
	while (disparo == 0):
		disparo = random.randint(-5,5)
	if a%2 == 0:
		return str(disparo)+",0"
	else:
		return "0,"+str(disparo)
	#return disparo_x + "," + disparo_y
