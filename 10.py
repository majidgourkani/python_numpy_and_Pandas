#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:52:29 2019
this is about Pandas(2)
@author: majid
"""

import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(4,5),['a','b','c','d'],[1,2,3,4,5])
df
df>0
b = df>0
b
df[b]
df[df>0]
df[1]>0
df[df[1]>0]
df[df[5]<0]

result = df[df[1]>0]
result[[3,4]]
df[df[1]>0][[3,4]]

df
df[(df[5]>0) & (df[4]>0)]
df[(df[5]>0) | (df[3]>0)]
#indexing

df
df.reset_index()
new_index = "T E S M".split()
new_index
df['new_column']=new_index
df
df.set_index('new_column')
df
df.set_index('new_column',inplace=True)
df