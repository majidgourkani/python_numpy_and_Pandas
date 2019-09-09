#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:02:15 2019
this is about Dataframe indexing(1)
@author: majid
"""

import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

ots = ['G1','G1','G1','G2','G2','G2']
ins = [1,2,3,1,2,3]
high_index = list(zip(ots,ins))
high_index
high_index = pd.MultiIndex.from_tuples(high_index)
high_index

df = pd.DataFrame(randn(6,2),high_index,['A','B'])
df
df.loc['G2'].loc[3]['B']

df.index.names
df.index.names = ['Outer_gorup','Inder_group']
df

df.loc['G1']
df.xs('G1')
df.xs(2,level='Inder_group')
#####################################################################

dic = {'A':[1,2,np.nan],'B':[np.nan,2,3],'C':[7,8,9]}
dic
df = pd.DataFrame(dic)
df
df.dropna()
df.dropna(axis=0)

df.fillna("majid")
df
df['A'].fillna("majid") 
