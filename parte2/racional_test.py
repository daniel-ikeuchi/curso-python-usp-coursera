# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:58:54 2019

@author: Daniel
"""
from racional import Racional

class TestRacional:
    
    def test_str(self):
        r = Racional(1, 2)
        assert r.__str__() == '1/2'
        
    def test_add(self):
        r1 = Racional(1, 2)
        r2 = Racional(3, 2)
        a = r1 + r2
        assert a.__str__() == '2'
    
    def test_sub(self):
        r1 = Racional(3, 2)
        r2 = Racional(1, 2)
        s = r1 - r2
        assert s.__str__() == '1'
       
    def test_mul(self):
        r1 = Racional(3, 2)
        r2 = Racional(1, 2)
        m = r1 * r2
        assert m.__str__() == '3/4'
        
    def test_mul_zero(self):
        r1 = Racional(3, 2)
        r2 = Racional(0)
        m = r1 * r2
        assert m.__str__() == '0'
    
    def test_div(self):
        r1 = Racional(3, 2)
        r2 = Racional(1, 2)
        d = r1 / r2
        assert d.__str__() == '3'
        
    def test_div_if_r1_zero(self):
        r1 = Racional()
        r2 = Racional(1, 2)
        d = r1 / r2
        assert d.__str__() == '0'
        
    def test_div_if_r2_zero(self):
        r1 = Racional(1, 2)
        r2 = Racional()
        d = r1 / r2
        assert d == 'Error'
        
    def test_den_equal_one(self):
        r = Racional(3)
        assert r.__str__() == '3'
        
    def test_den_not_equal_one(self):
        r = Racional(3, 2)
        assert r.__str__() == '3/2'
