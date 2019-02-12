# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:26:24 2019

@author: daniel
"""

from random import randint

def lista_grande(n):
    '''
    (int) -> list
    Retorna uma lista contendo n números insteiros aleatórios
    '''
    
    lista = []
    
    for i in range(n):
        lista.append(randint(-100, 100))
        
    return lista