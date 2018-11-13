#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:59:20 2018

@author: gabriel
"""

from params import params
from micsoreazaLatime import micsoreazaLatime
from micsoreazaInaltime import micsoreazaInaltime
from maresteLatime import maresteLatime

def redimensioneazaImagine():
	#redimensioneaza imaginea
	#
	#input: img - imaginea initiala
	#       parametri - stuctura de defineste modul in care face redimensionarea 
	#
	# output: imgRedimensionata - imaginea redimensionata obtinuta
	
	if params.optiuneRedimensionare == 'micsoreazaLatime':
		micsoreazaLatime()
			       
	elif params.optiuneRedimensionare == 'micsoreazaInaltime':
		micsoreazaInaltime()
