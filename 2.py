#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:10:14 2019
This is about inheritens
@author: majid
"""

class sport():
    def __init__(self, name):
        self.name = name
        print("This is sport and I'm {}." .format(self.name))
    def exitment(self):
        print("I'm excited.")
    def ntr(self,enter=""):
        print("dear {}, you are in new entertayment.".format(enter))
        
sp = sport("majid")
sp.exitment()
sp.ntr()


class football(sport):
    def __init__(self, name):
        sport.__init__(self, name)
        print("now we are in the football")

apf = football("majid")

apf.exitment()