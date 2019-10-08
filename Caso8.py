import random
import sys
import Sector
import datetime
from Sector import *
from PIL import Image

sys.setrecursionlimit(1000000000)

import math
import random
import sys
import Sector
from Sector import *
from Color import *
from PIL import Image

sys.setrecursionlimit(1000000000)

negro = Color("Negro", (0, 0, 0))
azul = Color("Azul", (0, 0, 255))
verde = Color("Verde", (0, 255, 0))
celeste = Color("Celeste", (0, 255, 255))
rojo = Color("Rojo", (255, 0, 0))
morado = Color("Morado", (255, 0, 255))
amarillo = Color("Amarillo", (255, 255, 0))


def resetColores():
    negro.cantidad = 0
    azul.cantidad = 0
    verde.cantidad = 0
    celeste.cantidad = 0
    rojo.cantidad = 0
    morado.cantidad = 0
    amarillo.cantidad = 0


def distance(xCord1, xCord2, yCord1, yCord2):
    sq1 = (xCord1 - xCord2) ** 2
    sq2 = (yCord1 - yCord2) ** 2
    return math.sqrt(sq1 + sq2)


def getColor(pX, pY):
    im = Image.open('garfield.jpg')  # Can be many different formats.
    pix = im.load()
    return pix[pX, pY]  # Get the RGBA Value of the a pixel of an image


def agregarPixel(x, y, cuadrante, color):
    listaColores = cuadrante.listaColores
    colorcito = ""
    if color[0] <= 127:
        if color[1] <= 127:
            if color[2] <= 127:
                if not negro in listaColores:
                    listaColores.append(negro)
                colorcito = "Negro"
            else:
                if not azul in listaColores:
                    listaColores.append(azul)
                colorcito = "Azul"
        else:
            if color[2] <= 127:
                if not verde in listaColores:
                    listaColores.append(verde)
                colorcito = "Verde"
            else:
                if not celeste in listaColores:
                    listaColores.append(celeste)
                colorcito = "Celeste"
    else:
        if color[1] <= 127:
            if color[2] <= 127:
                if not rojo in listaColores:
                    listaColores.append(rojo)
                colorcito = "Rojo"
            else:
                if not morado in listaColores:
                    listaColores.append(morado)
                colorcito = "Morado"
        else:
            if not amarillo in listaColores:
                listaColores.append(amarillo)
            colorcito = "Amarillo"
    listaColores[cuadrante.findByName(colorcito)].cantidad += 1
    cuadrante.listPixels.append(Pixel(x, y, colorcito))


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
    for cuadrante in listaSectores:
        for cant_Muestras in range(0, muestra):
            print("Cuadrante Probabilidad: ", cuadrante.probability)
            if cuadrante.probability > randomProbability:
                randomX = random.randint(cuadrante.xMin, cuadrante.xMax)
                randomY = random.randint(cuadrante.yMin, cuadrante.yMax)
                color = getColor(randomX, randomY)
                if color[0] <= 254 and color[1] <= 254 and color[2] <= 254:
                    agregarPixel(randomX, randomY, cuadrante, color)
                else:
                    cuadrante.probability -= 0.05
                print(cuadrante.porcentajePorColor())


def mapearSector(cantMuestras, pCantDiv):
    tamanoCuadrante = int(1023 / pCantDiv)
    listaSectores = crearSectores(pCantDiv, tamanoCuadrante)
    muestra = round(cantMuestras * 0.5)
    for cant in range(0, 5):
        randomProbability = random.uniform(0.1, 1.1)
        print("I: ",cant,"Random:",randomProbability)
        mapearMuestra(muestra, randomProbability, listaSectores)
    for sector in listaSectores:
        sector.porcentajePorColor()


def sampleo(pCantDiv, pPorcentaje):
    im = Image.open('garfield.jpg')
    cantMuestras = obtenerMuestras(pCantDiv, pPorcentaje)
    mapearSector(cantMuestras, pCantDiv)


def pintarCuadricula(pX, pY, pImage):
    pix = pImage.load()
    pix[pX, pY] = (0, 100, 0)


sampleo(4, 0.00001)
