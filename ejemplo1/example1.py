# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:14:52 2016

@author: marlonvinan
"""

import numpy as np
import matplotlib as p
import pdb
import pandas as pd

data = pd.read_csv('train.csv')

data

# primero separamos los dataframes por género

men = data[data.Sex == 'male']

women = data[data.Sex =='female']

# proporción de muejres que sobrevivieron

proportion_women_survived = float(sum(women.Survived))/len(women)

# proporción de hombres que sobrevivieron

proportion_men_survived = float(sum(men.Survived))/len(men)

# una alternativa de calcular es utilizando el método mean

proportion_bySex_survived = data.groupby('Sex').Survived.mean()

# para ver las columnas 

data.columns

# para ver la primera fila usamos el método xs(0)

data.xs(0)

# Vamos a crear una nueva columna para almacenar la predicción si alguien pudo haber 
# sobrevivido dependiendo del ambiente

data['Prediction']=0

# Si decimos que todos las mujeres sobrevivieron hacemos los siguiente>:

data.Prediction[data.Sex == 'female']=1

###### SEGUNDA PARTE #########

# vamos a encontrar la probabilidad de supervivencia de toda la gente en una combinación de
# género, clase social y precio del boleto 
# Primero vamos a reducir el precio del ticket  en categorías de: 0-9, 10-19, 20-29 y >30

data['soporte_tarifa']=0

data.soporte_tarifa = np.array([min(int(price/10),3) for price in data.Fare])

# vemos la distribución de acuerdo a la clase en la que viajaban

data.Pclass.hist()

look_up=dict()
for sex in unique(data.Sex):
    for pclass in unique(data.Pclass):
        for fare_bracket in unique(data.soporte_tarifa):
            look_up[(sex, pclass, soporte_tarifa)]= mean(data.Survived[(data.Sex == sex) & 
                           (data.Pclass == pclass) & (data.soporte_tarifa == fare_bracket)])
                           
                           




