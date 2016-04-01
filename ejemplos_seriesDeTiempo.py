# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:52:01 2016

@author: marlonvinan
"""

import pandas as pd
import numpy as np


from datetime import time


# TRABAJANDO CON SERIES DE TIEMPO

# Esta serie posee 3 valores aleatorios y sus indices son fechas cuya frecuencia se indica
# mediante 'W-WED' que especifica el próximo miércoles de la semana. Por último los periodos
# o filas son 3
ts1 = pd.Series(np.random.randn(3), index=pd.date_range('2016-3-29', periods=3, freq='W-WED'))

# si tu quieres transformar la serie anterior a una frecuencia que especifique los días
# laborables de la semana se usa el método reample('B').mean()

ts1.resample('B').mean()

# Si se quiere llenar los valores faltantes hay que el método ffill()

ts1.resample('B').mean().ffill()

# OTRO EJEMPLO

dates = pd.DatetimeIndex(['2016-3-30', '2016-4-6', '2016-4-13', '2016-4-20', '2016-4-27', 
'2016-5-4'])

ts2 = pd.Series(np.random.randn(6), index = dates)

# Si tu quieres agregar a partir de los valores ts1 llenando hacia adelante a ts2 manteniendo 
# las fechas como indices en ts2 se puede usar el método "reindex"

ts1.reindex(ts2.index, method='ffill')

ts2 + ts1.reindex(ts2.index, method='ffill')

###### USANDO PERIODOS DE TIEMPO ###########

# series financieras o económicas que trabajan con una frecuencia anual o trimestral

# Considere un par de series temporales macroeconómicas relacionadas con el PIB y la inflación

pib = pd.Series([1.79, 1.94, 2.08, 2.01, 2.15, 2.31, 2.46], 
                index = pd.period_range("1984Q2", periods = 7, freq='Q-SEP'))

infl = pd.Series([0.025, 0.045, 0.037, 0.04], 
                 index = pd.period_range('1982', periods=4, freq = "A-DEC"))

infl_q = infl.asfreq('Q-SEP', how='end')

# reindexar 

infl_q.reindex(pib.index, method='ffill')

############ uso de HORA DEL DIA #########################

rng = pd.date_range('2012-06-01 09:30', '2012-06-01 15:59', freq='T')
# Make a 5-day series of 9:30-15:59 values
rng = rng.append([rng + pd.offsets.BDay(i) for i in range(1, 4)])

ts = pd.Series(np.arange(len(rng), dtype=float), index=rng)

# indexando con datetime.time se puede extraer valores de determinados tiempos. Por ejemplo:
ts[time(10, 0)]
ts.at_time(time(10, 0))

# es posible seleccionar valores entre un rango específico, de la siguiente manera:

ts.between_time(time(10, 0), time(10, 1))

############ SPLICING TOGETHER DATA SOURCES ###########

# PRIMER ENFOQUE SWITCHING 

data1 = pd.DataFrame(np.ones((6, 3), dtype=float), columns=['a', 'b', 'c'], 
                  index=pd.date_range('30/3/2016', periods=6))

data2 = pd.DataFrame(np.ones((6, 3), dtype=float) * 2, columns=['a', 'b', 'c'],
                  index=pd.date_range('31/3/2016', periods=6))

spliced = pd.concat([data1.ix[:'2016-3-31'], data2.ix['2016-4-1':]])

# Segundo caso: datos faltantes

data2 = pd.DataFrame(np.ones((6, 4), dtype=float) * 2, columns=['a', 'b', 'c', 'd'], 
                     index=pd.date_range('6/13/2012', periods=6))


spliced = pd.concat([data1.ix[:'2012-06-14'], data2.ix['2012-06-15':]])

# combinar con data2

spliced_filled = spliced.combine_first(data2)

# TERCER CASO: Sustitución de datos

cp_spliced = spliced.copy()

cp_spliced[['a', 'c']] = data1[['a', 'c']]

cp_spliced



