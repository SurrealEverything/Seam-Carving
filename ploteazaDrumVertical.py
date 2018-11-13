#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:11:55 2018

@author: gabriel
"""
#import numpy as np
import matplotlib.pyplot as plt
from params import params
#from cv2fixed import imshowfixed
import cv2 

def ploteazaDrumVertical(E, drum):
	#ploteaza drumul vertical in imagine
	#
	#input: img - imaginea initiala
	#       E - energia la fiecare pixel calculata pe baza gradientului
	#       drum - drumul ce leaga sus de jos
	#       culoareDrum  - specifica culoarea cu care se vor plota pixelii din drum. Valori posibile:
	#                    [r g b]' - triplete RGB (e.g [255 0 0]' - rosu)          
	
	imgDrum = params.img
	imgDrum = cv2.cvtColor(imgDrum, cv2.COLOR_BGR2RGB)
	#E = cv2.cvtColor(E, cv2.COLOR_BGR2RGB)
	
	(h,) = drum.shape
	for i in range(h):
		imgDrum[i, drum[i], :] = params.culoareDrum
	
	
	plt.figure()
	
	plt.subplot(1, 2, 1)
	plt.imshow(imgDrum)
	plt.title('Drum')
	
	plt.subplot(1, 2, 2)
	plt.imshow(E, cmap='gray')
	plt.title('Energie')
	
	plt.show()