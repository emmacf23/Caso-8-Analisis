import math
import random
import sys
import Sector
from Sector import *
from Color import *
from GeneticAlgorithm import *
from PIL import Image

sys.setrecursionlimit(1000000000)


def distance(xCord1, xCord2, yCord1, yCord2):
    sq1 = (xCord1 - xCord2) ** 2
    sq2 = (yCord1 - yCord2) ** 2
    return math.sqrt(sq1 + sq2)


def getColor(pX, pY):
    im = Image.open('Pikachu.jpg')  # Can be many different formats.
    pix = im.load()
    return pix[pX, pY]  # Get the RGBA Value of the a pixel of an image


def agregarPixel(x, y, cuadrante, color):
    if color[0] <= 127:
        if color[1] <= 127:
            if color[2] <= 127:
                cuadrante.aumentarNegros()
            else:
                cuadrante.aumentarAzules()
        else:
            if color[2] <= 127:
                cuadrante.aumentarVerde()
            else:
                cuadrante.aumentarCeleste()
    else:
        if color[1] <= 127:
            if color[2] <= 127:
                cuadrante.aumentarRojo()
            else:
                cuadrante.aumentarMorado()
        else:
            cuadrante.aumentarAmarillo()
    cuadrante.listPixels.append(Pixel(x, y, color))


def obtenerMuestras(cantDivisiones, porcentaje):
    return round(1024 * 1024 / cantDivisiones * porcentaje)


def crearSectores(cantDiv, pLengthSector):
    xMin = 0
    yMin = 0
    yMax = pLengthSector
    xMax = pLengthSector
    listaSectores = []
    for fila in range(1, cantDiv + 1):
        for columna in range(1, cantDiv + 1):
            listaSectores.append(Sector(xMin, xMax, yMin, yMax))
            xMin += pLengthSector
            xMax += pLengthSector
        xMin = 0
        xMax = pLengthSector
        yMin += pLengthSector
        yMax += pLengthSector
    return listaSectores


def mapearMuestra(muestra, randomProbability, listaSectores):
    probabilidad = 0.0

    for cuadrante in listaSectores:
        for cant_Muestras in range(0, muestra):
            if cuadrante.probability > randomProbability:
                randomX = random.randint(cuadrante.xMin, cuadrante.xMax)
                randomY = random.randint(cuadrante.yMin, cuadrante.yMax)
                color = getColor(randomX, randomY)
                if color[0] <= 254 and color[1] <= 254 and color[2] <= 254:
                    agregarPixel(randomX, randomY, cuadrante, color)
                    probabilidad += 0.008
                else:
                    probabilidad -= 0.05
                #print("Color: ", color)
                #print(" Y: ", cuadrante.yMin, cuadrante.yMax, " X: ", cuadrante.xMin, cuadrante.xMax,
                #      "Cuadrante Probabilidad: ", cuadrante.probability)
        cuadrante.probability += probabilidad
        print("Cuadrante: ", cuadrante.probability)
        probabilidad = 0.0


def mapearSector(cantMuestras, pCantDiv):
    global svgStringGrande
    tamanoCuadrante = int(1023 / pCantDiv)
    listaSectores = crearSectores(pCantDiv, tamanoCuadrante)
    muestra = round(cantMuestras / 5)
    for cant in range(0, 5):
        randomProbability = random.uniform(0.1, 1.0)
        print("-----------------------------------------------------")
        print("I: ", cant, "Random:", randomProbability)
        mapearMuestra(muestra, randomProbability, listaSectores)
        print("-----------------------------------------------------")

    i = 1
    for sector in listaSectores:
        print('Sector', i)
        print('Cantidad Pixeles Sampleado por Sector: ', len(sector.listPixels))
        if len(sector.listPixels) != 0:
            sector.porcentajePorColor()
            Genetic(sector)
            print('------------------------------------------------------------------')
        i += 1

    terminarSVG()

def sampleo(pCantDiv, pPorcentaje):
    cantMuestras = obtenerMuestras(pCantDiv, pPorcentaje)
    print("Cant: ", cantMuestras)
    mapearSector(cantMuestras, pCantDiv)


def pintarCuadricula(pX, pY, pImage):
    pix = pImage.load()
    pix[pX, pY] = (0, 100, 0)


sampleo(12, 0.0005)
