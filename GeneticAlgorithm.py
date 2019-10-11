from Cromosoma import *
from Sector import *
from Rango import *
import random
from scipy.spatial import distance

genesSet = []
svgStringGrande = '<!DOCTYPE html>\n' + '<html>\n' + '<body>\n' + '<svg height = "1024" width = "1024">\n'


def sacarRangosCromosomas(pSector):
    global genesSet
    cantidadCromosomas = (2 ** 8) - 1
    cromosomaMinimo = 0
    listaRangos = []
    genesSet = pSector.matrizColores[0]
    for color in pSector.matrizColores[0]:
        if color.porcentage > 0:
            cromosomaMaximo = int(cromosomaMinimo + cantidadCromosomas * color.porcentage / 100)
            print('CromosomaMinimo:', cromosomaMinimo, 'CromosomaMaximo:', cromosomaMaximo, "Porcentaje:",
                  color.porcentage)
            rango = Rango(color, cromosomaMinimo, cromosomaMaximo)
            listaRangos.append(rango)
            cromosomaMinimo = cromosomaMaximo + 1

    return listaRangos


'''
def crearPoblacion(listaRangos, sector, cantidadPoblacion):
    global genesSet
    poblacion = []
    # for i in range(0,len(cantidadPoblacion)):
    xMin = sector.xMin
    xMax = sector.xMax
    yMin = sector.yMin
    yMax = sector.yMax
    poblacion = []
    for i in range(0, len(cantidadPoblacion)):
        # for rango in listaRangos:
        randomColor = random.randint(0, len(genesSet))
        randomX = random.randint(xMin, xMax)
        randomY = random.randint(yMin, yMax)
        poblacion.append(Cromosoma(randomColor, randomX, randomY))

    return poblacion
'''


def crearPoblacion(pListRanges, pSector, pQuantPoblation):
    global genesSet
    poblacion = []
    xMin = pSector.xMin
    xMax = pSector.xMax
    yMin = pSector.yMin
    yMax = pSector.yMax
    for i in range(0, pQuantPoblation):
        x = random.randint(0, ((2 ** 16) - 1))
        randomColor = genesSet[random.randint(0, len(genesSet) - 1)]
        p1 = (random.randint(xMin - 10, xMax + 10), random.randint(yMin - 10, yMax + 10))
        p2 = (random.randint(xMin - 10, xMax + 10), random.randint(yMin - 10, yMax + 10))
        p3 = (random.randint(xMin - 10, xMax + 10), random.randint(yMin - 10, yMax + 10))
        p4 = (random.randint(xMin - 10, xMax + 10), random.randint(yMin - 10, yMax + 10))
        poblacion.append(Cromosoma(x, p1, p2, p3, p4, randomColor))
    return poblacion


def averageSimilitud(pPoblacion, pObjetivo):
    average = 0
    for individuo in pPoblacion:
        average += getSimilitud(individuo, pObjetivo)

    return average / len(pPoblacion)


def getSimilitud(pIndividuo, pObjetivo):
    # return distance.euclidean(pIndividuo, pObjetivo)
    return 0


def obtenerFitness(pIndividuo, pObjetivo, pPoblacion):
    return averageSimilitud(pPoblacion, pObjetivo) > averageSimilitud(pPoblacion, pObjetivo) * getSimilitud(pIndividuo,
                                                                                                            pObjetivo)


"""
def ordenarLista(listaRangos):
    listaNueva = []
    min = 100
    for rango in listaRangos:
        if()
"""

def cuantos_digitos(n):
    ind = 1
    while n > 9:
        n = n / 10
        ind = ind + 1
    return ind
def crossover(pListFit):
    for indice in (0, len(pListFit/2)):
        cromosoma1 = bin(pListFit[indice].genes)
        cromosoma1 = bin(pListFit[indice + 1].genes)
        corte = random.randint(0,cuantos_digitos(cromosoma1))



def sacarExtremos(poblacion):
    extremos = []
    for i in range(0, 4):
        randomI = random.randint(0, len(poblacion))
        extremos.append(poblacion[randomI])


def sacarSVG(poblacion):
    global svgStringGrande
    svgString = "<polygon points= " + '"'
    for cromosoma in poblacion:
        svgString = svgString + str(cromosoma.point1[0]) + ',' + str(cromosoma.point1[1]) + ' '
        svgString = svgString + str(cromosoma.point2[0]) + ',' + str(cromosoma.point2[1]) + ' '
        svgString = svgString + str(cromosoma.point3[0]) + ',' + str(cromosoma.point3[1]) + ' '
        svgString = svgString + str(cromosoma.point4[0]) + ',' + str(cromosoma.point4[1]) + ' '
        svgString = svgString + '" style =' + '" fill: rgb' + str(
            cromosoma.Color.rgb) + ';stroke:black;stroke-width:1 "/>'
        svgStringGrande = svgStringGrande + svgString + "\n"
        svgString = "<polygon points= " + '"'


def Genetic(pSector):
    listaRangos = sacarRangosCromosomas(pSector)
    listaRangos.sort(key=lambda x: x.porcentage, reverse=True)
    newlist = sorted(listaRangos, key=lambda x: x.porcentage, reverse=True)
    print(newlist)
    poblacion = crearPoblacion(listaRangos, pSector, 10)
    sacarSVG(poblacion)
    aptos = []
    for cromosoma in poblacion:
        if obtenerFitness(cromosoma, newlist[0], poblacion):
            aptos.append(cromosoma)
            print("Cromosoma: ", cromosoma.Color, " P1:", cromosoma.point1, " P2:", cromosoma.point2, " P3:",
                  cromosoma.point3, " P4:", cromosoma.point4)


def terminarSVG():
    global svgStringGrande
    svgStringGrande = svgStringGrande + '</svg>\n' + '</body>\n' + '</html>\n'

    with open("poligonos.html", "w") as file:
        file.write(svgStringGrande)
