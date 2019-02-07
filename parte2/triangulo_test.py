# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:42:39 2019

@author: daniel
"""

import triangulo

class TestTriangulo:
    
    def test_perimetro(self):
        t = triangulo.Triangulo(3, 4, 5)
        assert t.perimetro() == 12
        
    def test_tipo_lado_equilatero(self):
        t = triangulo.Triangulo(3, 3, 3)
        assert t.tipo_lado() == 'equilátero'
        
    def test_tipo_lado_isosceles(self):
        t = triangulo.Triangulo(3, 3, 4)
        assert t.tipo_lado() == 'isósceles'
        
    def test_tipo_lado_escaleno(self):
        t = triangulo.Triangulo(3, 4, 5)
        assert t.tipo_lado() == 'escaleno'
        
    def test_retangulo_true(self):
        t = triangulo.Triangulo(3, 4, 5)
        assert t.retangulo() == True
    
    def test_retangulo_false(self):
        t = triangulo.Triangulo(4, 4, 5)
        assert t.retangulo() == False
        
    def test_semelhantes_true(self):
        t = triangulo.Triangulo(3, 4, 5)
        assert t.semelhantes(triangulo.Triangulo(6, 8, 10)) == True
        
    def test_semelhantes_false(self):
        t = triangulo.Triangulo(3, 4, 5)
        assert t.semelhantes(triangulo.Triangulo(6, 8, 11)) == False