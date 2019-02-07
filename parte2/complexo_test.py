# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:46:23 2019

@author: daniel
"""

import complexo

class TestComplexo:
    
    def test_soma(self):
        c1 = complexo.Complexo(3, 5)
        s = c1.soma(complexo.Complexo(1, -2))
        
        assert s.r == 4
        assert s.i == 3
        
    def test_multiplicacao(self):
        c1 = complexo.Complexo(3, 5)
        m = c1.multiplicacao(complexo.Complexo(1, -2))
        
        assert m.r == 13
        assert m.i == -1
              