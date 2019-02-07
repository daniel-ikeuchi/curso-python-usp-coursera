# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:40:09 2019

@author: daniel
"""

class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        else:
            return 'isósceles'
        
    def retangulo(self):
        if self.a ** 2 == self.b ** 2 + self.c ** 2\
           or self.b ** 2 == self.a ** 2 + self.c ** 2\
           or self.c ** 2 == self.a ** 2 + self.b ** 2:
             return True
        else:
             return False
         
    def semelhantes(self, triangulo):
        lados_t1 = [self.a, self.b, self.c]
        lados_t2 = [triangulo.a, triangulo.b, triangulo.c]
        
        lados_t1.sort()
        lados_t2.sort()
        
        # Cálculo fator de multiplicação
        fator =  lados_t1[0] // lados_t2[0]
        maior = 't1'
        
        if fator == 0:
            fator = lados_t2[0] // lados_t1[0]
            maior = 't2'
            
        # Verifica semelhança
        if maior == 't1':
            if lados_t1[1] % lados_t2[1] == 0\
               and lados_t1[2] % lados_t2[2] == 0:
                return True
            else:
                return False
        else:
            if lados_t2[1] % lados_t1[1] == 0\
               and lados_t2[2] % lados_t1[2] == 0:
                return True
            else:
                return False
            
        
        