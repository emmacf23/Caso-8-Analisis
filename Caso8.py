import sys
from PIL import Image
from GeneticAlgorithm import *
from Imagen import *
from Sector import *

sys.setrecursionlimit(1000000000)


def getColor(pX, pY, imgName):
    im = Image.open(imgName)  # Can be many different formats.
    pix = im.load()
    return pix[pX, pY]  # Get the RGBA Value of the a pixel of an image


def addPixel(pX, pY, pQuadrant, pColor):
    color = pQuadrant.arbol.searchColor(pColor)
    if color.nombre != "Blanco":
        color.cantidad += 1
        pQuadrant.listPixels.append(Pixel(pX, pY, pColor))


def obtainSample(pQuantDivi, porcentage):
    return round(1024 * 1024 / pQuantDivi * porcentage)


def createSectors(pQuantDiv, pLengthSector):
    xMin = 0
    yMin = 0
    yMax = pLengthSector
    xMax = pLengthSector
    sectorList = []
    i = 0
    for fila in range(1, pQuantDiv + 1):
        for columna in range(1, pQuantDiv + 1):
            sectorList.append(Sector((fila, columna), xMin, xMax, yMin, yMax))
            xMin += pLengthSector
            xMax += pLengthSector
            i += 1
        xMin = 0
        xMax = pLengthSector
        yMin += pLengthSector
        yMax += pLengthSector
    return sectorList


def mapSample(pSample, randomProbability, pSectorList, imgName):
    probability = 0.0
    for quadrant in pSectorList:
        for cant_Sample in range(0, pSample):
            if quadrant.probability > randomProbability:
                randomX = random.randint(quadrant.xMin, quadrant.xMax - 1)
                randomY = random.randint(quadrant.yMin, quadrant.yMax - 1)
                color = getColor(randomX, randomY, imgName)
                if color[0] <= 254 and color[1] <= 254 and color[2] <= 254:
                    addPixel(randomX, randomY, quadrant, color)
                    probability += 0.009
                else:
                    probability -= 0.06
        quadrant.probability += probability
        probability = 0.0


def mapSector(pQuantSample, pQuantDiv):
    global svgStringGrande
    imagenes = []
    listImage = ["coku.jpeg", "Pikachu.jpg", "spiderman.png"]
    # for imgName in listImage:
    sectorList = createSectors(pQuantDiv, round(1023 / pQuantDiv))
    sample = round(pQuantSample / 3)
    for cant in range(1, 3):
        print(cant)
        randomProbability = random.uniform(0.1, 1.0)
        mapSample(sample, randomProbability, sectorList, listImage[0])
    imagenes.append(Imagen(listImage[1], sectorList))
    # for img in imagenes:
    #print(img.name)
    for j in range(1, 10):
        i = 1
        for sector in imagenes[1].sectores:
            print('Sector', i)
            if len(sector.listPixels) != 0:
                sector.porcentajePorColor()
                Genetic(sector, j)
            i += 1
        if j % 1 == 0 or j == 1:
            terminarSVG(j)


def sampling(pQuantDiv, pPorcentage):
    quantSample = obtainSample(pQuantDiv, pPorcentage)
    print("Cant: ", quantSample)
    mapSector(quantSample, pQuantDiv)


def paintCuadricula(pX, pY, pImage):
    pix = pImage.load()
    pix[pX, pY] = (0, 100, 0)


sampling(64, 0.0002)
