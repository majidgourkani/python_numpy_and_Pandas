#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 23:00:17 2019
this is about numpy(2)
@author: majid
"""

import numpy as np

ar = np.arange(0,10)
ar
ar[0:5]
ar[:8]
ar[:3] = 1000
br = ar[1:6]
br
br[:] = 99
br
ar
cr = ar.copy()
cr[:3] = 101
cr
ar

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr
arr[1][2]
arr[1,2]
arr[0:2,0:2]

dr = np.arange(0,10)
dr
dr+dr
dr*3
dr+50
dr/dr
1/dr
