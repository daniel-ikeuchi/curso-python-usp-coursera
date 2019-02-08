# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:45:29 2019

@author: Daniel
"""
def mdc(a, b):
    ''' 
    (int, int) -> int
    recebe dois inteiros diferentes de zero e retorna o maximo
    divisor comum entre a e b
    '''
    if b == 0: return a
    if a == 0: return b
    
    while a % b != 0:
        a, b = b, a % b
        
    return b

class Racional:
    
    def __init__(self, num = 0, den = 1):
        m = mdc(num, den)
        self.put(num / m, den / m)
        
    def __str__(self):
        if self.den != 1:
            return '%d/%d'%(self.num, self.den)
        else:
            return '%d'%(self.num)
    
    def get(self):
        return self.num, self.den
    
    def put(self, num, den):
        self.num, self.den = num, den
        
    def __add__(self, other):
        den = self.den * other.den
        num = den / self.den * self.num + den / other.den * other.num
        return Racional(num, den)
    
    def __sub__(self, other):
        den = self.den * other.den
        num = den / self.den * self.num - den / other.den * other.num
        return Racional(num, den)
    
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Racional(num, den)
    
    def __truediv__(self, other):
        if other.__str__() == '0':
            return 'Error'
        else:
            num = self.num * other.den
            den = self.den * other.num
            return Racional(num, den)
    
    