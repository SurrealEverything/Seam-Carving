#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:12:12 2018

@author: gabriel
"""

from params import params
import numpy as np

def eliminaDrumVertical(drum):
	#elimina drumul vertical din imagine
	#input: img - imaginea initiala
	#       drum - drumul vertical
	#output img1 - imaginea initiala din care s-a eliminat drumul vertical
	h, w, c = params.img.shape
	print(h, w-1, c)
	for i in range(h):
		coloana = drum[i]
		#copiem partea din dreapta
		params.img[i, coloana:w-1, :] = params.img[i, coloana+1:w, :]
		
	params.img = np.delete(params.img, -1, axis=1)