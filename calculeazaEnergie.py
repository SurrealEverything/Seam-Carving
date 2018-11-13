#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:11:27 2018

@author: gabriel
"""

from params import params
import cv2
import numpy as np

def calculeazaEnergie():
	#calculeaza energia la fiecare pixel pe baza gradientului
	#input: img - imaginea initiala
	#output: E - energia
	
	#urmati urmatorii pasi:
	#transformati imaginea in grayscale
	greyImg = cv2.cvtColor(params.img, cv2.COLOR_BGR2GRAY)
	
	#folositi un filtru sobel pentru a calcula gradientul in directia x si y
	dx = cv2.Sobel(greyImg, cv2.CV_64F, 1, 0, ksize=5)
	dy = cv2.Sobel(greyImg, cv2.CV_64F, 0, 1 , ksize=5)
	
	
	#E - energia = gradientul imaginii
	E = np.empty(greyImg.shape, dtype='uint8')
	E = cv2.convertScaleAbs(dx) + cv2.convertScaleAbs(dy)
	
	return E