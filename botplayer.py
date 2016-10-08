import numpy
import random

"""
	0,1 hacia abajo
	-1,0 hacia izq
	1,0 hacia der
	0,-1 hacia arriba
"""

def calcularCuadrante(cuadrante, mayorAmen = 0):
	print "Calcular Cuadrante:", cuadrante, mayorAmen
	if cuadrante == 0:
		if mayorAmen == 1 or mayorAmen == 0:
			return "0,-2"
		elif mayorAmen == 2:
			return "0,-1"
		elif mayorAmen == 3:
			return "0,-3"		
	elif cuadrante == 1:
		if mayorAmen == 1 or mayorAmen == 0:
			return "-2,0"
		elif mayorAmen == 2:
			return "-1,0"
		elif mayorAmen == 3:
			return "-3,0"
	elif cuadrante == 2:
		if mayorAmen == 1 or mayorAmen == 0:
			return "0,2"
		elif mayorAmen == 2:
			return "-0,1"
		elif mayorAmen == 3:
			return "0,3"
	elif cuadrante == 3:
		if mayorAmen == 1 or mayorAmen == 0:
			return "2,0"
		elif mayorAmen == 2:
			return "1,0"
		elif mayorAmen == 3:
			return "3,0"

def calcularDisparo(cuadrante, mayorAmen = 0):
	print "Calcular disparo:", cuadrante, mayorAmen
	if cuadrante == 0:
		if 0 <= mayorAmen <= 1:
			if (random.randint(1,2)%2 == 0):
				return "0,-5"
			else:
				return "0,-4"
		if mayorAmen == 2:
			if (random.randint(1,2)%2 == 0):
				return "0,-3"
			else:
				return "0,-2"
		if mayorAmen == 3:
			return "0,-1"
	elif cuadrante == 1:
		if 0 <= mayorAmen <= 1:
			if (random.randint(1,2)%2 == 0):
				return "-5,0"
			else:
				return "-4,0"
		if mayorAmen == 2:
			if (random.randint(1,2)%2 == 0):
				return "-3,0"
			else:
				return "-2,0"
		if mayorAmen == 3:
			return "-1,0"
	elif cuadrante == 2:
		if 0 <= mayorAmen <= 1:
			if (random.randint(1,2)%2 == 0):
				return "0,5"
			else:
				return "0,4"
		if mayorAmen == 2:
			if (random.randint(1,2)%2 == 0):
				return "0,3"
			else:
				return "0,2"
		if mayorAmen == 3:
			return "0,1"
	elif cuadrante == 3:
		print "Ubicado en el cuadrante 3"
		if 0 <= mayorAmen <= 1:
			if (random.randint(1,2)%2 == 0):
				return "5,0"
			else:
				return "4,0"
		if mayorAmen == 2:
			if (random.randint(1,2)%2 == 0):
				return "3,0"
			else:
				return "2,0"
		if mayorAmen == 3:
			return "1,0"
		
	
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
					
#def escoger_disparo( amenazas ):
	#disparo_x = ""
	#disparo_y = ""
#	amenazas = amenazas.strip().split(':')
#	a = random.randint(1,2)
#	disparo = 0
#	while (disparo == 0):
#		disparo = random.randint(-5,5)
#	if a%2 == 0:
#		return str(disparo)+",0"
#	else:
#		return "0,"+str(disparo)
#	#return disparo_x + "," + disparo_y
	
def escoger_disparo(amenazas):
	amenazas = amenazas.strip().split(':')
	if len(amenazas) == 1:
		return calcularDisparo(random.randint(0,3))
	else:
		mayorCuad = -1
		mayorAmen = 0
		totalAmen = dict()
		amenDir = amenazas[0].split('-')
		for i in amenDir:
			if i in '123':
				if i not in totalAmen:
					totalAmen[i] = 0
				totalAmen[i] += 1
		amenCuad = amenazas[1].split('-')
		for i in range(len(amenCuad)):
			if mayorCuad < amenCuad[i]:
				mayorCuad = amenCuad[i]
				cuadMayor = i
		for i in totalAmen:
			if i > mayorAmen:
				mayorAmen = i
		return calcularDisparo(cuadMayor,mayorAmen)
		
							
