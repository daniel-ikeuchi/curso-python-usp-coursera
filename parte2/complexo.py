# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:42:01 2019

@author: daniel
"""
import math

class Complexo:
    
    def __init__(self, r = 0, i = 0):
        self.r = r
        self.i = i
        
    def soma(self, c):
        s = Complexo()
        
        s.r = self.r + c.r
        s.i = self.i + c.i
        
        return s
    
    def multiplicacao(self, c):
        m = Complexo()
        
        real = self.r * c.r + self.i * c.i * (-1)
        img = self.r * c.i + self.i * c.r
        
        m.r = real
        m.i = img
        
        return m
    
    def __str__(self):
        if self.i > 0:
            return '%s + %si'%(self.r, self.i)
        else:
            return '%s - %si'%(self.r, abs(self.i))