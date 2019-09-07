#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:36:48 2019
This is about Special methods
@author: majid
"""

class account():
    def __init__(self, name, acc, amount):
        self.name = name
        self.acc = acc
        self.amount = amount

    def __str__(self):
        return "{} , ACC num is {}, ${}".format(self.name,self.acc,self.amount)

    def __len__(self):
        return self.amount
    
    def __del__(self):
        return "this account is deleted"
    
my_acc = account("majid",123,90000)
print(my_acc)
str(my_acc)
len(my_acc)
del(my_acc)
str(my_acc)