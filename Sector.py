import Pixel
from Pixel import *
# from ArbolColores import *
from arbolNario import *


class Sector:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.listPixels = []
        self.porcentageColor = 0.0
        self.probability = 1.0
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.matrizColores = [
            [negro, azulOscuro, azul, verdeOscuro, turquesaOscuro, azulClaro, verde, verdeClaro, celeste, vino, morado,
             purpura, gris, lila, lima, limaClaro, celesteClaro, rojo, fucsia, rosado, naranja, paloRosa, pink,
             amarillo,
             amarilloClaro, amarilloVerdoso, blanco],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.poblacion = []

    def increaseBlack(self):
        self.matrizColores[1][0] += 1

    def increaseDarkBlue(self):
        self.matrizColores[1][1] += 1

    def increaseBlue(self):
        self.matrizColores[1][2] += 1

    def increaseDarkGreen(self):
        self.matrizColores[1][3] += 1

    def increaseDarkTurquoise(self):
        self.matrizColores[1][4] += 1

    def increaseLigthBlue(self):
        self.matrizColores[1][5] += 1

    def increaseGreen(self):
        self.matrizColores[1][6] += 1

    def increaseLigthGreen(self):
        self.matrizColores[1][7] += 1

    def increaseCeleste(self):
        self.matrizColores[1][8] += 1

    def increaseWine(self):
        self.matrizColores[1][9] += 1

    def increasePurple(self):
        self.matrizColores[1][10] += 1

    def increasePurpura(self):
        self.matrizColores[1][11] += 1

    def increaseGrey(self):
        self.matrizColores[1][12] += 1

    def increaseLile(self):
        self.matrizColores[1][13] += 1

    def increaseLime(self):
        self.matrizColores[1][14] += 1

    def increaseLigthLime(self):
        self.matrizColores[1][15] += 1

    def increaseLightLightBlue(self):
        self.matrizColores[1][16] += 1

    def increaseRed(self):
        self.matrizColores[1][17] += 1

    def increaseFuchsia(self):
        self.matrizColores[1][18] += 1

    def increaseRose(self):
        self.matrizColores[1][19] += 1

    def increaseOrange(self):
        self.matrizColores[1][20] += 1

    def increasePaloRosa(self):
        self.matrizColores[1][21] += 1

    def increasePink(self):
        self.matrizColores[1][22] += 1

    def increaseYellow(self):
        self.matrizColores[1][23] += 1

    def increaseLigthYellow(self):
        self.matrizColores[1][24] += 1

    def increaseYellowGreen(self):
        self.matrizColores[1][25] += 1


    def getPixels(self):
        return self.listPixels

    def printPixels(self):
        for pixel in self.listPixels:
            print("(" + str(pixel.getCordX()) + "," + str(pixel.getCordY()) + ") " + str(pixel.getColor()))

    def getPorcentage(self):
        return self.porcentageColor

    def setPixels(self, pixels):
        self.listPixels = pixels

    def porcentaje(self):
        R = 0
        G = 0
        B = 0
        i = 0
        for pixel in self.listPixels:
            R = R + pixel.getColor()[0]
            G = G + pixel.getColor()[1]
            B = B + pixel.getColor()[2]
            i = i + 1
        if i == 0:
            return (255, 255, 255)
        else:
            return (R / i, G / i, B / i)

    def getPoints(self):
        pixelsPoligono = []
        for pixel in self.listPixels:
            pixelsPoligono.append(pixel)

        return pixelsPoligono

    def porcentajePorColor(self):
        cantSample = len(self.listPixels)
        largoColor = 0
        while largoColor < len(self.matrizColores[0]):
            color = self.matrizColores[0][largoColor]
            cantColors = self.matrizColores[1][largoColor]
            if cantSample > 0:
                color.porcentage = 100 / cantSample * cantColors
                if color.porcentage > 0:
                    print("Cantidad Color:", cantColors)
                    print("Color: ", color.nombre, " Porcentaje: ", color.porcentage)
            largoColor += 1
