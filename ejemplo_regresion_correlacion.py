# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:07:21 2016

@author: marlonvinan
"""

#Regresion lineal y correlación

import pandas.io.data as web

aapl = web.get_data_yahoo('AAPL', '2000-01-01')['Adj Close']
msft = web.get_data_yahoo('MSFT', '2000-01-01')['Adj Close']

#La correlación es una manera de mirar el co-movimiento entre los cambios
# en dos series temporales de activos

# La función rolling_corr con dos series de tiempo para poder compararlas
# Comparamos APPLE y Microsoft

aapl_rets = aapl.pct_change()
msft_rets = msft.pct_change()

pd.rolling_corr(aapl_rets, msft_rets, 250).plot()

# utilizando el modelo de minimos cuadrados para regresión lineal
model = pd.ols(y=aapl_rets, x={'MSFT': msft_rets}, window=250)
 
 model.beta

model.beta['MSFT'].plot()
