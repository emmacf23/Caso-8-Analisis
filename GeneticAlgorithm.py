from Cromosoma import *
from Sector import *
from Rango import *
import random
from scipy.spatial import distance

genesSet = []
svgStringGrande = '<!DOCTYPE html>\n' + '<html>\n' + '<body>\n' + '<svg height = "1024" width = "1024">\n'
cantidadCromosomas = (2**8) - 1


def sacarRangosCromosomas(pSector):
    global genesSet,cantidadCromosomas
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



def crearPoblacion(pListRanges, pSector, pQuantPoblation):
    global genesSet,cantidadCromosomas
    poblacion = []
    xMin = pSector.xMin
    xMax = pSector.xMax
    yMin = pSector.yMin
    yMax = pSector.yMax
    for i in range(0, pQuantPoblation):
        x = random.randint(0, cantidadCromosomas)
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
    return distance.euclidean(pIndividuo.Color.rgb, pObjetivo.color.rgb)
    #return 0


def obtenerFitness(pIndividuo, pObjetivo, pPoblacion):
    return averageSimilitud(pPoblacion, pObjetivo) > averageSimilitud(pPoblacion, pObjetivo) * getSimilitud(pIndividuo,
                                                                                                            pObjetivo)

def cuantos_digitos(n):
    ind = 1
    while n > 9:
        n = n / 10
        ind = ind + 1
    return ind

def isBitOn(pDescendant, pivot):
    if pDescendant & (1 << pivot):
        print("SET")
        return True
    else:
        print("NO SET")
        return False


def mutation(pDescendant, pivot, set):
    """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
    mask = 1 << pivot  # Compute mask, an integer with just bit 'index' set.
    pDescendant &= ~mask  # Clear the bit indicated by the mask (if x is False)
    if set:
        pDescendant |= mask  # If x was True, set the bit indicated by the mask.
    return pDescendant  # Return the result, we're done.



def crossover(pParent1,pParent2):
    global cantidadCromosomas
    pivotParent2 = random.randint(3,6)
    pivotParent1 = 8 - pivotParent2
    #print("Pivot1:",pivotParent2,"Pivot2:",pivotParent1)
    descendant = ((pParent1>>pivotParent2)<<pivotParent2) | (((pParent2<<pivotParent1) & cantidadCromosomas)>>pivotParent1)
    #print(descendant)
    probMutation = random.randint(0,100)
    if probMutation < 5:
        bit = random.randint(0,8)
        if isBitOn(descendant,bit):
            mutation(descendant,bit,1)
        else:
            mutation(descendant,bit,0)
        print("C muto xd")

    return descendant



def sacarSVG(poblacion):
    global svgStringGrande
    svgString = "<polygon points= " + '"'
    for cromosoma in poblacion:
        svgString = svgString + str(cromosoma.point1[0]) + ',' + str(cromosoma.point1[1]) + ' '
        svgString = svgString + str(cromosoma.point2[0]) + ',' + str(cromosoma.point2[1]) + ' '
        svgString = svgString + str(cromosoma.point3[0]) + ',' + str(cromosoma.point3[1]) + ' '
        svgString = svgString + str(cromosoma.point4[0]) + ',' + str(cromosoma.point4[1]) + ' '
        svgString = svgString + '" style =' + '" fill: rgb' + str(
            cromosoma.Color.rgb) + '"/>'
        svgStringGrande = svgStringGrande + svgString + "\n"
        svgString = "<polygon points= " + '"'


def sacarAptos(poblacion,listaRangos):
    aptos = []
    for cromosoma in poblacion:
        if obtenerFitness(cromosoma, listaRangos[0], poblacion):
            print("|||||||||||||||||||||||||||||||||||||||||||")
            #print(cromosoma)
            aptos.append(cromosoma)
            print("Cromosoma: ", cromosoma.Color, " P1:", cromosoma.point1, " P2:", cromosoma.point2, " P3:",
                  cromosoma.point3, " P4:", cromosoma.point4)

    return aptos

def generateDescendant(pSector,pNewGenes,pColor):
    p1 = (random.randint(pSector.xMin - 10, pSector.xMax + 10), random.randint(pSector.yMin - 10, pSector.yMax + 10))
    p2 = (random.randint(pSector.xMin - 10, pSector.xMax + 10), random.randint(pSector.yMin - 10, pSector.yMax + 10))
    p3 = (random.randint(pSector.xMin - 10, pSector.xMax + 10), random.randint(pSector.yMin - 10, pSector.yMax + 10))
    p4 = (random.randint(pSector.xMin - 10, pSector.xMax + 10), random.randint(pSector.yMin - 10, pSector.yMax + 10))

    return Cromosoma(pNewGenes,p1,p2,p3,p4,pColor)

def Genetic(pSector):
    listaRangos = sacarRangosCromosomas(pSector)
    listaRangos = sorted(listaRangos, key=lambda x: x.porcentage, reverse=True)
    poblacion = crearPoblacion(listaRangos, pSector, 15)
    sacarSVG(poblacion)
    aptos = sacarAptos(poblacion,listaRangos)
    print("Before:", aptos)
    if len(aptos) <= 1:
        print("Hay uno o menos aptos")
    else:
        for i in range(0,len(aptos)):
            #if obtenerFitness(crossover(aptos[i].genes,aptos[i+1].genes),listaRangos[0],poblacion):
            newGenes = crossover(aptos[i].genes,aptos[i+1].genes)
            newColor = listaRangos[0].color
            newDescendant = generateDescendant(pSector,newGenes,newColor)
            aptos.append(newDescendant)
            print("Holi")
            print(newDescendant)
            i += 1

    print("After:",aptos)


def terminarSVG():
    global svgStringGrande
    svgStringGrande = svgStringGrande + '</svg>\n' + '</body>\n' + '</html>\n'

    with open("poligonos.html", "w") as file:
        file.write(svgStringGrande)
