#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:58:34 2018

@author: gabriel
clear"""

#import numpy as np
import cv2
import matplotlib.pyplot as plt
from redimensioneazaImagine import redimensioneazaImagine
from params import params

#Implementarea a proiectului Redimensionare imagini
#dupa articolul "Seam Carving for Content-Aware Image Resizing", autori S.
#Avidan si A. Shamir 
##
#aceasta functie ruleaza intregul proiect 
redimensioneazaImagine() 
imgRedimensionata_proiect = params.img

#foloseste functia resize pentru redimensionare traditionala
(h, w, c) = params.img.shape
imgRedimensionata_traditional = cv2.resize(params.imgReferinta, (w, h), cv2.INTER_CUBIC)
	
#denumim pozele	
if params.metodaSelectareDrum == 'aleator':
	metSel = 'Aleator'
elif params.metodaSelectareDrum == 'greedy':
	metSel = 'Greedy'
elif params.metodaSelectareDrum == 'programareDinamica':
	metSel = 'PD'

if params.optiuneRedimensionare == 'micsoreazaInaltime':
	optRed = str(params.numarPixeliInaltime) 
	optRed += 'MicIn'
elif params.optiuneRedimensionare == 'micsoreazaLatime':
	optRed = str(params.numarPixeliLatime) 
	optRed += 'MicLat'


numeImgProiect = params.numeImg + metSel + optRed + 'Proiect.' + params.tipImg
numeImgTraditional = params.numeImg + optRed + 'Traditional.' + params.tipImg

#scriem imaginile
cv2.imwrite(numeImgProiect, imgRedimensionata_proiect)
cv2.imwrite(numeImgTraditional, imgRedimensionata_traditional)

#convertim BGR to RGB pentru matplotlib
imgReferinta = cv2.cvtColor(params.imgReferinta, cv2.COLOR_BGR2RGB)
imgRedimensionata_proiect = cv2.cvtColor(imgRedimensionata_proiect, cv2.COLOR_BGR2RGB)
imgRedimensionata_traditional = cv2.cvtColor(imgRedimensionata_traditional, cv2.COLOR_BGR2RGB)

#ploteaza imaginile obtinute
plt.figure()

#1. imaginea initiala
plt.subplot(1, 3, 1)
plt.imshow(imgReferinta)
plt.xlabel('imaginea initiala')

#2. imaginea redimensionata cu pastrarea continutului
plt.subplot(1, 3, 2)
plt.imshow(imgRedimensionata_proiect)
plt.xlabel('rezultatul nostru')

#3. imaginea obtinuta prin redimensionare traditionala
plt.subplot(1, 3, 3)
plt.imshow(imgRedimensionata_traditional)
plt.xlabel('rezultatul imresize')

plt.show()