#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 08:51:14 2019

@author: valeria
"""

temp = int(input('Entre com a temperatura: '))
if temp < 0:
    print('Congelando...')
elif 0 <= temp <= 20:
    print('Frio...')
elif 21 <= temp <= 25:
    print('Normal')
elif 26 <= temp <= 35:
    print('Quente')
else:
    print('Muito quente')