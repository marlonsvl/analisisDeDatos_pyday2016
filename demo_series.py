# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:56:42 2016

@author: marlonvinan
"""
import numpy as np
import pandas as pd

# Uso de resample y reindex

ts1 = pd.Series(np.random.randn(3), index=pd.date_range('2012-6-13', periods=3, freq='W-WED'))

# remodelar usando resample para todos los dias laborables de la semana

ts1.resample('B')


# El método ffill para llenar los valores nulos

ts1.resample('B').ffill()

# reindex

dates = pd.DatetimeIndex(['2012-6-12', '2012-6-17', '2012-6-18', '2012-6-21', 
                             '2012-6-22', '2012-6-29'])

ts2 = pd.Series(np.random.randn(6), index=dates)

ts2
# reindexar los valores de ts1 con ts2

ts1.reindex(ts2.index, method='ffill')