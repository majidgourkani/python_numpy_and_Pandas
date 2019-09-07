#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:12:32 2019
this is about Abstract Class
@author: majid
"""

class docu():
    def __init__(self,name):
        self.name = name
    def show(self):
        raise NotImplementedError("SunClass most Implemented method...!!!")
        
doc1 = docu("pdf")
doc1.show()

class pdf(docu):
    def show(self):
        print("pdf content is here...!!")

class word(docu):
    def show(self):
        print("word content is here...!!")

pdf1 = pdf("pdf test")
word1 = word("word test")

pdf1.show()
word1.show()