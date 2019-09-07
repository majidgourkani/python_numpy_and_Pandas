#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:02:16 2019
This is about numpy(1)
@author: majid
"""

import numpy as np

a = [1,2,3,4,5]
b = np.array(a)

c = [[1,2,3],[4,5,6],[7,8,9]]
d = np.array(c)

np.arange(1,10)
np.arange(1,10,3)
np.zeros(4)
np.zeros((3,4))
np.ones((4,4))
np.linspace(1,20,7)
np.eye(5)
np.random.rand(5)
np.random.rand(5,5)
np.random.randn(20,20)
np.random.randint(1,200)

e = np.arange(20)
e.shape
f = e.reshape(4,5)
f.shape

arr = np.random.randint(1,100,15)
arr
arr.max()
arr.min()
arr.argmax()
arr.argmin()










