import Pixel
from Pixel import *
from collections import Counter


class Sector:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.listPixels = []
        self.porcentageColor = 0.0
        self.probability = 1
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.listaColores = []

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
        cantidadMuestra = len(self.listPixels)
        for color in self.listaColores:
            print("Cantidad: ", color.cantidad, "Cantidad muestra: ", cantidadMuestra)
            color.porcentage = color.cantidad / cantidadMuestra * 100
            print("Color: ", color.nombre, " Porcentaje: ", color.porcentage)

        #print("Entre x=", self.xMin, "y x=", self.xMax)
        #print("Entre y=", self.yMin, "y y=", self.yMax)

    def findByName(self,nombre):
        for color in self.listaColores:
            if color.nombre == nombre:
                return self.listaColores.index(color)