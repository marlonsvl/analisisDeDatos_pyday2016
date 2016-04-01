# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:41:24 2016

@author: marlonvinan
"""

# En un contexto financiero "returns o rendimiento" se refiere a porcentajes de cambio en el 
# precio de un activo

# Vamos a considerar los datos de precios de ACTIVOS de Apple en 2011 hasta el  2016

import pandas.io.data as web

price = web.get_data_yahoo('AAPL', '2011-01-01')['Adj Close']

returns = price.pct_change()

ret_index = (1 + returns).cumprod()

ret_index[0] = 1 # Primer valor se fija en 1 1

# Con un índice de rentabilidad en la mano, el cálculo de los rendimientos acumulados en una 
#determinada resolución es simple 

m_returns = ret_index.resample('BM').last().pct_change()

m_returns['2016']

