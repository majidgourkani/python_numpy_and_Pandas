#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:02:04 2019
This is about Polimorphism
@author: majid
"""

class dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says WOOOF!!"

class cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says MEOOO!!"

d1 = dog("Rex")
c1 = cat("cyti")

print(d1.speak())
print(c1.speak())

for pet in [d1,c1]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())
    
pet_speak(d1)
pet_speak(c1)
