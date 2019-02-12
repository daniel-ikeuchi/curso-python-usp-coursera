# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:00:34 2019

@author: daniel
"""

def busca(lista, elemento):
    '''
    (list, obj) -> int
    Dada uma lista e um elemento, retorna a posição do elemento na
    lista, caso esteja na lista ou retorna False caso não esteja na
    lista.
    '''
    
    for posicao in range(len(lista)):
        if lista[posicao] == elemento:
            return posicao
    return False