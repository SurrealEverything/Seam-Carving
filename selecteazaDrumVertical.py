#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:11:39 2018

@author: gabriel
"""
from params import params
import numpy as np
def selecteazaDrumVertical(E):
	#selecteaza drumul vertical ce minimizeaza functia cost calculate pe baza lui E
	#
	#input: E - energia la fiecare pixel calculata pe baza gradientului
	#       metodaSelectareDrum - specifica metoda aleasa pentru selectarea drumului. Valori posibile:
	#                           'aleator' - alege un drum aleator
	#                           'greedy' - alege un drum utilizand metoda Greedy
	#                           'programareDinamica' - alege un drum folosind metoda Programarii Dinamice
	#
	#output: d - drumul vertical ales(d[coloana]=linie)
	hE, wE = E.shape
	
	d = np.empty((hE,), dtype='uint16')
	
	if params.metodaSelectareDrum == 'aleator':
		#pentru linia 0 alegem primul pixel in mod aleator
		#coloana o alegem intre 1 si size(E,2)		
		#punem in d coloana coresponzatoare pixelului
		d[0] = np.random.randint(wE)
		for i in range (1, hE):
			#alege urmatorul pixel pe baza vecinilor
			#linia este i
			#coloana depinde de coloana pixelului anterior
			if d[i-1] == 0:#pixelul este localizat la marginea din stanga
				#doua optiuni
				optiune = np.random.randint(1)#genereaza 0 sau 1 cu probabilitati egale 
			elif d[i-1] == wE-1:#pixelul este la marginea din dreapta
				#doua optiuni
				optiune = np.random.randint(1) - 1 #genereaza -1 sau 0
			else:
				optiune = np.random.randint(2) - 1 # genereaza -1, 0s sau 1
					
			# merg la stanga, dreapta sau stau pe loc
			#adun -1 sau 0 sau 1:
			d[i] =  d[i-1] + optiune 
		       
	elif params.metodaSelectareDrum == 'greedy':
		#pentru linia 0 alegem cel mai mare pixel
		#coloana o alegem intre 1 si size(E,2)		
		#punem in d coloana coresponzatoare pixelului
		d[0] = E[0].argmin()
		for i in range (1, hE):
			st = d[i-1] - 1
			mij = d[i-1]
			dr = d[i-1] + 1
			
			if d[i-1] == 0:#pixelul este localizat la marginea din stanga
				#doua optiuni
				optiune = E[i][[mij, dr]].argmin()
			elif d[i-1] == wE-1:#pixelul este la marginea din dreapta
				#doua optiuni
				optiune = E[i][[st, mij]].argmin() - 1
			else:
				#genereaza -1, 0s sau 1
				optiune = E[i][[st, mij, dr]].argmin() - 1
					
			# merg la stanga, dreapta sau stau pe loc
			#adun -1 sau 0 sau 1:
			d[i] =  d[i-1] + optiune 
		
	elif params.metodaSelectareDrum == 'programareDinamica':
		
		inf = np.iinfo(np.uint32).max
		costE = np.full((hE, wE), inf, dtype='uint32')
		
		costE[0, :] = E[0, :]
		
		for i in range(1, hE):
			for j in range(wE):
				st = j-1
				mij = j
				dr = j+1
				
				if j == 0:
					costE[i, j] = costE[i-1, [mij, dr]].min() + E[i, j]
				elif j == wE-1: 
					costE[i, j] = costE[i-1, [st, mij]].min() + E[i, j]
				else:
					costE[i, j] = costE[i-1, [st, mij, dr]].min() + E[i, j]
			
		d[hE-1] = costE[hE-1].argmin()
		
		#print(costE[hE-1])
		
		for i in range(hE-2, -1, -1):
			#print('\nstart for\ni==', i)
			st = d[i+1] - 1
			mij = d[i+1]
			dr = d[i+1] + 1
			#print('mij==', mij)
			if mij == 0:
				#print('costE==', costE[i, [mij, dr]])
				optiune = costE[i, [mij, dr]].argmin()
			elif mij == wE-1:
				optiune = costE[i, [st, mij]].argmin() - 1
			else:
				#print('costE==', costE[i, [mij, dr]])
				optiune = costE[i, [st, mij, dr]].argmin() - 1
			
			#print ('optiune==', optiune)
			
			d[i] =  mij + optiune
			#print('d[i]==', d[i])	
		
	else:
		print('Optiune pentru metodaSelectareDrum invalida')
	
	return d