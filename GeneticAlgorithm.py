import random
import math

from Cromosoma import *
from Rango import *

genesSet = []
pivot = 0
svgStringGrande = '<!DOCTYPE html>\n' + '<html>\n' + '<body>\n' + '<svg height = "1024" width = "1024">\n'
cantidadCromosomas = (2 ** 8) - 1


def genNumRan(begin1, end1, begin2, end2):
    return random.randint(begin1, end1), random.randint(begin2, end2)


def getChromoRange(pSector):
    global genesSet, cantidadCromosomas
    cromosomaMinimo = 0
    listaRangos = []
    for color in pSector.colores:
        color = pSector.arbol.searchColor(color.rgb)
        if color.porcentage > 0:
            cromosomaMaximo = math.floor(cromosomaMinimo + cantidadCromosomas * color.porcentage / 100)

            print('CromosomaMinimo:', cromosomaMinimo, 'CromosomaMaximo:', cromosomaMaximo, "Porcentaje:",
                  color.porcentage)
            rango = Rango(color, cromosomaMinimo, cromosomaMaximo)
            listaRangos.append(rango)
            cromosomaMinimo = cromosomaMaximo + 1
    return listaRangos


def sacarColorRango(pGen, pListRanges):
    for rangeX in pListRanges:
        if (rangeX.cromosomaMinimo <= pGen < rangeX.cromosomaMaximo) or (
                rangeX.cromosomaMinimo < pGen <= rangeX.cromosomaMaximo):
            return rangeX.color


def crearPoblacion(pListRanges, pSector, pQuantPoblation):
    global genesSet, cantidadCromosomas
    xMin = pSector.xMin - 10
    xMax = pSector.xMax + 10
    yMin = pSector.yMin - 10
    yMax = pSector.yMax + 10
    lista = random.sample(range(cantidadCromosomas), pQuantPoblation)
    for i in range(0, pQuantPoblation):
        color = sacarColorRango(lista[i], pListRanges)
        # print("Color", color)
        pSector.poblacion.append(
            Cromosoma(lista[i], genNumRan(xMin, xMax, yMin, yMax), genNumRan(xMin, xMax, yMin, yMax),
                      genNumRan(xMin, xMax, yMin, yMax), genNumRan(xMin, xMax, yMin, yMax), color))


def averageSimilitud(pPoblacion, pObjetivo):
    average = 0
    for individuo in pPoblacion:
        average += getSimilitud(individuo, pObjetivo)
    return average / len(pPoblacion)


def getSimilitud(pIndividuo, pObjetivo):
    return abs(pObjetivo - pIndividuo.genes)


def aplicarFitness(pIndividuo, pObjetivo, pPoblacion):
    pIndividuo.aptitud = getSimilitud(pIndividuo, pObjetivo) / pObjetivo


def cuantos_digitos(n):
    ind = 1
    while n > 9:
        n = n / 10
        ind = ind + 1
    return ind


def isBitOn(pDescendant, pivot):
    if pDescendant & (1 << pivot):
        return True
    else:
        return False


def mutation(pDescendant, pivot, set):
    mask = 1 << pivot
    pDescendant &= ~mask
    if set:
        pDescendant |= mask
    return pDescendant


def crossover(pParent1, pParent2):
    global cantidadCromosomas
    pivotParent2 = random.randint(3, 6)
    pivotParent1 = 8 - pivotParent2
    descendant = ((pParent1 >> pivotParent2) << pivotParent2) | (
            ((pParent2 << pivotParent1) & cantidadCromosomas) >> pivotParent1)
    probMutation = random.randint(0, 100)
    if probMutation < 5:
        bit = random.randint(0, 7)
        if isBitOn(descendant, bit):
            descendant = mutation(descendant, bit, 0)
        else:
            descendant = mutation(descendant, bit, 1)
    return descendant


def sacarSVG(poblacion):
    global svgStringGrande, pivot
    svgString = "<polygon points= " + '"'
    for cromosoma in poblacion:
        # print("Cromosoma: ", cromosoma)
        svgString = svgString + str(cromosoma.point1[0]) + ',' + str(cromosoma.point1[1]) + ' '
        svgString = svgString + str(cromosoma.point2[0]) + ',' + str(cromosoma.point2[1]) + ' '
        svgString = svgString + str(cromosoma.point3[0]) + ',' + str(cromosoma.point3[1]) + ' '
        svgString = svgString + str(cromosoma.point4[0]) + ',' + str(cromosoma.point4[1]) + ' '
        svgString = svgString + '" style =' + '" fill: rgb' + str(
            cromosoma.Color.rgb) + '"/>'
        svgStringGrande = svgStringGrande + svgString + "\n"
        svgString = "<polygon points= " + '"'



def obtenerAptos(poblacion, listaRangos):
    for cromosoma in poblacion:
        aplicarFitness(cromosoma, (listaRangos[0].cromosomaMinimo + listaRangos[0].cromosomaMaximo / 2), poblacion)


def sacarAptos(poblacion, listaRangos):
    obtenerAptos(poblacion, listaRangos)
    poblacion.sort(key=lambda x: x.aptitud, reverse=False)
    poblacion = sorted(poblacion, key=lambda x: x.aptitud, reverse=False)
    # print("Poblacion:", poblacion)
    aptos = []
    for i in range(0, round(len(poblacion) / 2)):
        aptos.append(poblacion[i])
    # print("Aptos:", aptos)
    return aptos


def generateDescendant(pSector, pNewGenes, pColor):
    return Cromosoma(pNewGenes, genNumRan(pSector.xMin - 10, pSector.xMax + 10, pSector.yMin - 10, pSector.yMax + 10),
                     genNumRan(pSector.xMin - 10, pSector.xMax + 10, pSector.yMin - 10, pSector.yMax + 10),
                     genNumRan(pSector.xMin - 10, pSector.xMax + 10, pSector.yMin - 10, pSector.yMax + 10),
                     genNumRan(pSector.xMin - 10, pSector.xMax + 10, pSector.yMin - 10, pSector.yMax + 10), pColor)


def obtenerNuevaPoblacion(aptos, listaRangos, pSector):
    nuevaPoblacion = []
    if len(aptos) > 1:
        for i in range(0, round(len(aptos) / 2)):
            newGenes1 = crossover(aptos[i].genes, aptos[i + 1].genes)
            newGenes2 = crossover(aptos[i + 1].genes, aptos[i].genes)
            newDescendant1 = generateDescendant(pSector, newGenes1, sacarColorRango(newGenes1, listaRangos))
            newDescendant2 = generateDescendant(pSector, newGenes2, sacarColorRango(newGenes2, listaRangos))
            nuevaPoblacion.append(aptos[i])
            nuevaPoblacion.append(aptos[i + 1])
            nuevaPoblacion.append(newDescendant1)
            nuevaPoblacion.append(newDescendant2)
            i += 1
    pSector.poblacion = nuevaPoblacion


def Genetic(pSector, iteration):
    rangeList = getChromoRange(pSector)
    rangeList.sort(key=lambda x: x.porcentage, reverse=True)
    rangeList = sorted(rangeList, key=lambda x: x.porcentage, reverse=True)
    if pSector.poblacion == []:
        crearPoblacion(rangeList, pSector, 10)
    if iteration % 5 == 0 or iteration == 1:
        sacarSVG(pSector.poblacion)
    aptos = sacarAptos(pSector.poblacion, rangeList)
    obtenerNuevaPoblacion(aptos, rangeList, pSector)


def terminarSVG():
    global svgStringGrande
    svgStringGrande = svgStringGrande + '</svg>\n' + '</body>\n' + '</html>\n'
    with open("index" + ".html", "w") as file:
        file.write(svgStringGrande)
    svgStringGrande = '<!DOCTYPE html>\n' + '<html>\n' + '<body>\n' + '<svg height = "1024" width = "1024">\n'
