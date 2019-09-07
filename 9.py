#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 20:00:49 2019
this is about Pandas(1)
@author: majid
"""
import numpy as np
import pandas as pd

data = [10,20,30,40,50]
pd.Series(data)
labels = ['a', 'b', 'c', 'd', 'e']
pd.Series(data=data, index=labels)

ar = np.array(data)
ar
pd.Series(ar, labels)

dic = {'a':10, 'b':20, 'c':30, 'd':40}
pd.Series(dic)

li = ['a', 'b', 'c', 'd']
pd.Series(li)

sr1 = pd.Series([1,2,3,4,5],['a','b','c','d','e'])
sr1
sr2 = pd.Series([1,2,3,4,5],['c','b','a','d','e'])
sr2
sr1['a']
sr2['d']
sr1+sr2
sr3 = pd.Series([1,2,3,4,5])
sr1+sr3

#####################################################
#Data Frame

import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['a','b','c','D'])
df
df['a']
df['A']
type(df['a'])
type(df[['a','b']])
df1 = df[['a','b']]
df1
type(df1)
df1['new'] = [1,2,3,4,5]
df1
df1['next'] = df['c']+df['a']
df1
df.drop('a',axis=1)
df.drop('E',axis=0)
df
df.drop('a',axis=1,inplace=True)
df
df.loc['A']
df.iloc[1]
df.loc['A','c']
df.loc[['A','C','D'],['b','c']]
