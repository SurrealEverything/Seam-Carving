#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:11:17 2018

@author: gabriel
"""
from params import params
from calculeazaEnergie import calculeazaEnergie
from selecteazaDrumVertical import selecteazaDrumVertical
from ploteazaDrumVertical import ploteazaDrumVertical
from eliminaDrumVertical import eliminaDrumVertical
import matplotlib.pyplot as plt	
import time

def micsoreazaLatime():
#micsoreaza imaginea cu un numar de pixeli 'numarPixeliLatime' pe latime (elimina drumuri de sus in jos) 
#
#input: img - imaginea initiala
#       numarPixeliLatime - specifica numarul de drumuri de sus in jos eliminate
#       metodaSelectareDrum - specifica metoda aleasa pentru selectarea drumului. Valori posibile:
#                           'aleator' - alege un drum aleator
#                           'greedy' - alege un drum utilizand metoda Greedy
#                           'programareDinamica' - alege un drum folosind metoda Programarii Dinamice
#       ploteazaDrum - specifica daca se ploteaza drumul gasit la fiecare pas. Valori posibile:
#                    0 - nu se ploteaza
#                    1 - se ploteaza
#       culoareDrum  - specifica culoarea cu care se vor plota pixelii din drum. Valori posibile:
#                    [r g b]' - triplete RGB (e.g [255 0 0]' - rosu)          
#                           
# output: img - imaginea redimensionata obtinuta prin eliminarea drumurilor

	for i in range(params.numarPixeliLatime):
	
		print('Eliminam drumul vertical numarul ' + str(i+1) + ' dintr-un total de ' + str(params.numarPixeliLatime))
		
		#calculeaza energia dupa ecuatia (1) din articol
		E = calculeazaEnergie()
		
		#alege drumul vertical care conecteaza sus de jos
		drum = selecteazaDrumVertical(E)
		
		#afiseaza drum
		if params.ploteazaDrum:
			ploteazaDrumVertical(E, drum)
			time.sleep(0.1)
			plt.close()#needed?
			
			
		#elimina drumul din imagine
		eliminaDrumVertical(drum)


