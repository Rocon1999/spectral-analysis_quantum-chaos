"""
Título: Código análisis espectral
Autor: Rodrigo Fernández-Quevedo García
Año: 2022

Código utilizado para la realización del análisis del espectro de energía.

Para la implementación es necesario la utilización del módulo de elaboración 
propia con las funciones utilizadas: AnalisisEspectral.py
"""
#Paquetes utilizados
from matplotlib import pyplot as plt
import numpy as np
import AnalisisEspectral as An

######################### LIMPIEZA Y MAGNITUDES #########################
#Cargamos los datos, autovalores de energía del hamiltoniano, los ordenamos 
#ascendentemente y eliminamos el 5% mayor y menor.
eigen=An.LimpiezaDatos('Datos.dat', 5)
#Hallamos el espaciamiento entre niveles
gap=An.Gap(eigen)
#Hallamos los ratios entre niveles
ratios=An.CalculorRatios(gap)
#Hallamos los ratios mínimos
rmin=An.RatiosMinimos(ratios)
#Presentamos el promedio de los ratios y ratios mínimos
print(np.mean(ratios))
print(np.mean(rmin))
################################ UNFOLDING ##############################
#Realizamos el unfolding de los autovalores
eigen_unfold=An.unfolding(eigen,4)
#E
gap_unfold=An.Gap(eigen_unfold)
###
################################## FIGURAS #############################
############# Espaciamientos
#Según los datos que se analicen será necesario elegir el número de divisiones
#(div) del histograma y los límites (xi,xf) que sean convenientes
plt.figure()
An.HistogramaGap(gap_unfold, div, 'Histograma de espaciamiento',
                     'Espaciamiento entre niveles', xi,xf)
#Guardamos la figura en formato jpg
plt.savefig('Espaciamientos_K05.jpg',bbox_inches='tight')
#Realizamos la figura anterior en escala logarítmica
plt.figure()
mf.HistogramaGap(gap_unfold, div, 'Histograma de espaciamiento k=0.5',
                     'Espaciamiento entre niveles', xi,xf,scale='log')
#Guardamos la figura en formato jpg
plt.savefig('Espaciamientos_K05_log.jpg',bbox_inches='tight')
############### Ratios
#Según los datos que se analicen será necesario elegir el número de divisiones
#(div) del histograma y los límites (xi,xf) que sean convenientes
plt.figure()
mf.ratios(ratios,div,xi,xf,title='Histograma de ratios',col='blue')
#Guardamos la figura en formato jpg
plt.savefig('Ratios_K05.jpg',bbox_inches='tight')



