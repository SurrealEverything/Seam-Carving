#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:01:24 2018

@author: gabriel
"""

from params import params
from calculeazaEnergie import calculeazaEnergie
from selecteazaDrumVertical import selecteazaDrumVertical
from ploteazaDrumVertical import ploteazaDrumVertical
from eliminaDrumVertical import eliminaDrumVertical
import matplotlib.pyplot as plt	
import time
from scipy import ndimage

def micsoreazaInaltime():
#micsoreaza imaginea cu un numar de pixeli 'numarPixeliInaltime' pe inaltime (elimina drumuri din stanga in dreapta) 
#
#input: img - imaginea initiala
#       numarPixeliInaltime - specifica numarul de drumuri din stanga in dreapta eliminate
#       metodaSelectareDrum - specifica metoda aleasa pentru selectarea drumului. Valori posibile:
#                           'aleator' - alege un drum aleator
#                           'greedy' - alege un drum utilizand metoda Greedy
#       ploteazaDrum - specifica daca se ploteaza drumul gasit la fiecare pas. Valori posibile:
#                           'programareDinamica' - alege un drum folosind metoda Programarii Dinamice
#                    0 - nu se ploteaza
#                    1 - se ploteaza
#       culoareDrum  - specifica culoarea cu care se vor plota pixelii din drum. Valori posibile:
#                    [r g b]' - triplete RGB (e.g [255 0 0]' - rosu)          
#                           
# output: img - imaginea redimensionata obtinuta prin eliminarea drumurilor
	
	params.img = ndimage.rotate(params.img, 90)
	
	for i in range(params.numarPixeliInaltime):
	
		print('Eliminam drumul orizontal numarul ' + str(i+1) + ' dintr-un total de ' + str(params.numarPixeliInaltime))
		
		#calculeaza energia dupa ecuatia (1) din articol
		E = calculeazaEnergie()
		
		#alege drumul vertical care conecteaza sus de jos
		drum = selecteazaDrumVertical(E)
		
		#afiseaza drum
		if params.ploteazaDrum:
			ploteazaDrumVertical(E, drum)
			time.sleep(0.1)
			plt.close()
			
			
		#elimina drumul din imagine
		eliminaDrumVertical(drum)

	params.img = ndimage.rotate(params.img, 270)
