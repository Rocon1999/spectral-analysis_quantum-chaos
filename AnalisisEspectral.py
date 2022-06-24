"""
Título: Módulo de análisis espectral
Autor: Rodrigo Fernández-Quevedo García
Año: 2022

Módulo con las funciones necesarias para la realización del análisis del
conjunto de autovalores de un sistema. 
"""

import numpy as np
import csv
from matplotlib import pyplot as plt


def LimpiezaDatos(file,percent,modo=''):
    '''
    Carga los archivos, los lee guardando los datos en la variable Datos (en 
    caso de ser un archivo csv es necesario indicarlo en la entrada modo) y 
    limpia los datos ordenándolos ascendentemente y eliminando de los mismos 
    el porcentaje (percent) indicado tanto de los datos mayores como de los 
    menores.
    
    file: archivo de datos, válido como .txt y .csv
    percent: porcentaje de datos a quitar
    Clean_Datos: variable de salida que contiene los datos limpios
    '''
    LecDat=open(file,'r')#Abrimos el archifo
    Datos=LecDat.read() #Lo leemos y guardamos en la variable Evalues
    if (modo=='csv'):
        Datos=np.array(Datos.split(',')).astype(float)#Creamos un array
    else:
        Datos=np.array(Datos.split()).astype(float)#Creamos un array
    LecDat.close()#Cerramos el archivo de datos
    Datos.sort()#Ordenamos en forma ascendente
    
    XPercent=round(len(Datos)*percent/100) #Calculamos el X% de los elementos
    #Creamos un nuevo array sin el X% deseado
    Clean_Datos=Datos[XPercent:(len(Datos)-XPercent)]
    return Clean_Datos

def Gap(Datos):
    '''
    Halla el espaciamiento entre niveles de energía, autovalores.
    
    Datos: autovalores
    gap: espaciamiento entre autovalores
    '''
    gap=np.zeros([len(Datos)-1])#Vector que contendrá los espaciamientos

    for i in range(0,len(Datos)-1):
        #Calculamos las diferencias de energía entre los autovalores
        gap[i]=Datos[i+1]-Datos[i]
    return gap

def HistogramaGap(Datos, div,title,xlab,x0,x1,scale='normal',col='purple',norm='media'):
    '''
    Genera un histograma de el espaciamiento entre niveles.
    
    Datos: datos de los que realizar el histograma
    div: divisiones del histograma
    xlab: etiqueta del eje x
    x0, x1: Límites del eje x
    scale: por defecto utiliza una escala lineal, si se determina como 'log', 
    lo realizará en escala logarítmica
    
    Col: color del histograma, por defecto será morado
    norm: por defecto la normalización la realiza según la media de los datos, 
    si se indica max la realizará según el elemento mayor de los datos
    '''
    if norm=='media':#Normalización a la media+
        Datos=Datos/np.mean(Datos)
    if norm=='max' :#Normalización al máximo
        Datos=Datos/np.max(Datos)   
    plt.hist(Datos, bins=div, density=True, color=col,ec='black')#,density=True
    if scale=='log':
        plt.yscale("log")
    plt.title(title)
    plt.grid()
    plt.xlabel(xlab)
    plt.xlim(x0,x1)
    
    
def unfolding(Datos,n=3):
    '''
    Realiza un proceso de reescalado de los niveles de energía, eliminando 
    eliminando fluctuaciones locales y normalizándo los datos a la media 
    de los mismos. Par elllo halla la función espectral acumulativa e
    interpola la función a un polinomio de grado n, obteniendo una función suave.
    Finalmente, evalua los autovalores en dicho polinomio.
    
    Datos: secuencia de energias
    n: grado del polinomio al que interpolar, por defecto n=3
    e: autovalores reescalados
    '''
    #Normalizamos a la media
    Datos=Datos/np.mean(Datos)
    #Halamos la función espectral acumulativa
    eta=np.linspace(0,len(Datos),len(Datos))
    #Interpolación de la función espectral acumulativa
    p=np.polyfit(Datos,eta,n)
    #Evaluamos los puntos de los autovalores
    e=np.polyval(p,Datos)
    ###########
    return e
    
    
def CalculadorRatios(Datos):
    '''
    Realiza el cálculo de los ratios entre niveles a partir de los espaciamientos
    
    Datos: gaps entre los niveles de energía
    r: ratios de los gaps
    '''
    r=np.zeros(len(Datos)-1)#Vector que contendrá los ratios
    #Hallamos los ratios
    for i in range(0,len(Datos)-1):
        r[i]=Datos[i+1]/Datos[i]
    return r

def ratios(Datos,div,x0,x1,col='purple',title=''):
    '''
    Realiza un histograma de los ratios de espaciamiento entre niveles.
    
    Datos: ratios de los gaps
    div: intervalos presentes en el histograma
    x0, x1: límites del histograma, x0 inicial y x1 final.
    col: color del histograma, por defecto morado
    title: título que aparecerá en el histograma
    '''
    plt.hist(Datos, density = True, bins = div,range=(x0,x1), color=col,ec='black')
    plt.title(title)
    plt.xlabel('Ratios')
    plt.grid()
    plt.xlim((x0, x1))


def RatiosMinimos(Datos):
    '''
    Calcula los ratios mínimos, rmin=min(r,1/r)
    
    Datos: ratios del espaciamiento entre niveles
    '''
    rmin=np.zeros(len(Datos))
    for i in range(len(Datos)):
        rmin[i]=min(Datos[i],1./Datos[i])
    return rmin
