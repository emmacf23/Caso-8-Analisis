from Cromosoma import *
from Sector import *
from Rango import *
import random
from scipy.spatial import distance

genesSet = []

def sacarRangosCromosomas(pSector):
    global genesSet
    cantidadCromosomas = (2**16) - 1
    cromosomaMinimo = 0
    listaRangos = []
    genesSet = pSector.matrizColores[0]
    for color in pSector.matrizColores[0]:
        cromosomaMaximo = cromosomaMinimo + cantidadCromosomas * color.porcentage
        rango = Rango(color,cromosomaMinimo,cromosomaMaximo)
        listaRangos.append(rango)
        cromosomaMinimo = cromosomaMaximo + 1

    return listaRangos


def crearPoblacion(listaRangos,sector,cantidadPoblacion):
    global genesSet
    poblacion = []
    #for i in range(0,len(cantidadPoblacion)):
    xMin = sector.xMin
    xMax = sector.xMax
    yMin = sector.yMin
    yMax = sector.yMax
    poblacion = []
    for i in range(0,len(cantidadPoblacion)):
    #for rango in listaRangos:
        randomColor = random.randint(0,len(genesSet))
        randomX = random.randint(xMin, xMax)
        randomY = random.randint(yMin, yMax)
        poblacion.append(Cromosoma(randomColor,randomX,randomY))

    return poblacion


def averageSimilitud(pPoblacion,pObjetivo):
    average = 0
    for individuo in pPoblacion:
        average += getSimilitud(individuo,pObjetivo)

    return average/len(pPoblacion)


def getSimilitud(pIndividuo,pObjetivo):
    return distance.euclidean(pIndividuo, pObjetivo)

def obtenerFitness(pIndividuo,pObjetivo,pPoblacion):
    return averageSimilitud(pPoblacion,pObjetivo) > averageSimilitud(pPoblacion,pObjetivo) * getSimilitud(pIndividuo,pObjetivo)