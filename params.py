#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:17:33 2018

@author: gabriel
"""
import numpy as np
import cv2

#setati parametri si imaginile de redimensionat aici
class params:
	#puteti inlocui numele imaginii
	numeImg = 'castel'
	tipImg = 'jpg'
	#citeste imaginea care va fi transformata in mozaic	
	imgReferinta = cv2.imread('/home/gabriel/Spyder Projects/VA/Tema2/data/' + numeImg + '.' + tipImg)
	img = np.array(imgReferinta, copy=True) 
	drumuriDeAdaugat = []
	offsets = None
	#reducem imaginea in latime cu 20 de pixeli
	optiuneRedimensionare = 'micsoreazaLatime'
	
	numarPixeliInaltime = 50
	numarPixeliLatime = 0
	
	#0/1
	ploteazaDrum = 1
	
	#culoarea rosie
	culoareDrum = np.array([255, 0, 0])
	
	#optiuni posibile: 'aleator','greedy','programareDinamica'
	metodaSelectareDrum = 'programareDinamica'
	