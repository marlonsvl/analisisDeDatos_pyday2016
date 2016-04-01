# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

# users

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']

users = pd.read_table('/Users/marlonvinan/Documents/pyday/ml-1m/users.dat', sep='::', header=None,
names=unames, engine='python')

# ratings
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']

ratings = pd.read_table('/Users/marlonvinan/Documents/pyday/ml-1m/ratings.dat', sep='::', header=None,
names=rnames, engine='python')

# movies
mnames = ['movie_id', 'title', 'genres']

movies = pd.read_table('/Users/marlonvinan/Documents/pyday/ml-1m/movies.dat', sep='::', header=None,
names=mnames, engine='python')

#verifying

users[:5]

ratings[:5]

movies[:5]

ratings

# Analizar datos en 3 tablas puede ser muy complicado, por ejmplo suponga que
# queremos calcular la media de los ratings (mean ratings) de las peliculas por sexo
# y edad.

# 1ro Merge data

data = pd.merge(pd.merge(ratings, users), movies)

# 2do obtener el promedio de los ratings por sexo y edad
# (index por cols) para esta versión 

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

# VAMOS A FILTRAR LAS PELICULAS QUE HAN RECIVIDO POR LO MENOS 250 RATINGS

#PRIMERO: agrupar los datos por titulo y el tamaño de los mismos
ratings_by_title = data.groupby('title').size()

#LUEGO: se obtiene los títulos que cumplen con la restricción
active_titles = ratings_by_title.index[ratings_by_title >= 250]

# EL INDICE DE TITULOS RECIBIDOS QUE CUMPLEN CON LA RESTRICCIÓN DE POR LO MENOS 250 RATINGS
# PUEDE SER USADO PARA SELECCIONAR LAS FILAS DESDE mean_ratings.

mean_ratings = mean_ratings.ix[active_titles]

# para ver las películas mas vistas por chicas (F) vamos a ordenar tomando en cuenta la
# columna F en orden descentente

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

# DIVIDIR

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

# ver las peliculas que tienen mayor diferencia de audiencia y preferidas por mujeres
sorted_by_diff = mean_ratings.sort_values(by='diff')

# revirtiendo el orden obtenemos las 15 peliculas más rankeadas por los hombres
sorted_by_diff[::-1][:15]


# AHORA SUPONGA QUE SE QUIERE OBTENER LAS PELICULAS QUE HAN SUSCITADO poca APROBACIÓN
# ENTRE LOS FANÁTICOS INDEPENDIENTEMENTE DEL GÉNERO

# ESTO SE CALCULA UTILIZANDO VARIANZA O STANDARD DEVIATION

# se calcula la desviación estándar agropuado por titulo

rating_std_by_title = data.groupby('title')['rating'].std()

# filtramos nuevamente con los titulos que cumplen la restricción

rating_std_by_title = rating_std_by_title.ix[active_titles]

# ordenamos las series por valor en orden descendente

rating_std_by_title.sort_values(ascending=False)[:10]

# US Baby Names 1880-2010 nextttttttt














