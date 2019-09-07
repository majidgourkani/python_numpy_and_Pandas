#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:38:49 2019
this is about Pandas(series)
@author: majid
"""

import numpy as np
import pandas as pd

sri = [10,20,30,40,50,60,70]
lab = ['a','b','c','d','e','f','g']
pd.Series(sri,lab)

arr = np.array(sri)
arr
pd.Series(data=arr,index=lab)




