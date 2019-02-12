# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:40:17 2019

@author: daniel
"""

def ordenada(lista):
    '''
    (list) -> bool
    Recebe uma lista de inteiros e retorna True caso a lista esteja
    ordenada ou False, caso contrário.
    '''
    
    ordenada = True
    posicao = 0
    
    while ordenada and posicao < len(lista) - 1:
        if lista[posicao + 1] < lista[posicao]:
            ordenada = False
        posicao += 1
        
    return ordenada