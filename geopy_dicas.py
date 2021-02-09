# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 23:40:43 2019

@author: pliniobas
"""

#%%
from geopy.distance import distance,Point
dir(distance)

#%%Distancia entre 2 pontos
dis = distance((-24,-42),(-24.5,-42.5)).nm
print(dis, 'nm')
dis = distance((-24,-42),(-24.5,-42.5)).km #
print(dis,'km')


#%%fornece um novo ponto/offset, fornecendo uma distancia e um rumo em graus
dis = distance(nautical=15).destination((-24,-42),90)
print(dis,'nm')
dis = distance(kilometers=1).destination((-24,-42),0)
print(dis,'km')
help(distance) # para ver o nome das unidades de distancias

#%%Formata de DD.DD para DMS.SS

ponto = distance(nautical=1).destination((-24,-42),0)
print(dir(ponto))
print(help(ponto.format))
print("DMS = ",ponto.format()) #Passa de grau decimal (D) para grau minuto segundo (DMS)
print("DMS com grau = ", ponto.format(deg_char='°')) #Passa de grau decimal (D) ou DMS
print("DD.DD = ", ponto.format_decimal())

#%%Ponto a partir de uma string
p1 = Point('24 45.55m S, 45 0m 0s W')

p2 = Point.from_string('24 45m 30s S, 45 W')
print('p1 = ',p1)
print('p1 == p2?', p1 == p2)

print(p1.format(deg_char = "°", min_char= '\'' ,sec_char= "\""))
# %%

print(p1.format_decimal())
# %%

def dd2dms(dd):
    if dd < 0:
        dd = abs(dd)
        sinal = -1
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    return deg * sinal ,mnt,sec

print(dd2dms(p1.latitude))
#%%

def dd2dm(dd):
    if dd < 0:
        dd = abs(dd)
        sinal = -1
    deg,mnt = divmod(dd*60,60)
    return deg * sinal,mnt

print(dd2dm(p1.latitude))
#%% Dica do Piero para correção de direção de bussola
print(-45%360)
print(370%360)

# %%
print(p1.latitude)
temp = abs(p1.latitude) * 60
sec = temp % 60
min = sec % 60


print(temp,sec,min)

#%%

# %%
print(temp)
print(temp % 60)
print(temp // 60)
print(temp / 60)


#%%
from lat_lon_parser import parse

a = parse('-24 50.20')
print(a)
help(parse)


parse('24 40.753691 S')
parse('042 9.720168 W')

#%%
p1 = Point('25.2,43.25')
dd2dm(p1)
