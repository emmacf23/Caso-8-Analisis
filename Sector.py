import Pixel
from Color import Color
from Pixel import *
from ArbolColores import *


class Sector:
    def __init__(self,nombre, xMin, xMax, yMin, yMax):
        self.colores = self.crearColores()
        self.nombre = nombre
        self.listPixels = []
        self.porcentageColor = 0.0
        self.probability = 1.0
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.arbol = Node('ArbolColores', 0)
        self.arbol.armarArbolColores()
        self.arbol.fillColors(self.colores)
        self.poblacion = []

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
        #print("Sector:", self.nombre)
        #print("Cantidad:", cantSample)
        for color in self.colores:
            colorArbol = self.arbol.searchColor(color.rgb)
            #            print("Arbol",self.arbolColores)
            if cantSample > 0:
                colorArbol.porcentage = 100 / cantSample * colorArbol.cantidad
        #        if colorArbol.porcentage > 0:
         #           print("Cantidad Color:", colorArbol.cantidad)
        #          print("Color: ", colorArbol.nombre, " Porcentaje: ", colorArbol.porcentage)

    def crearColores(self):
        negro = Color("Negro", (0, 0, 0))
        azulOscuro = Color("AzulOscuro", (0, 0, 127))
        azul = Color("Azul", (0, 0, 255))

        verdeOscuro = Color("VerdeOscuro", (0, 127, 0))
        turquesaOscuro = Color("TurquesaOscuro", (0, 127, 127))
        azulClaro = Color("AzulClaro", (0, 127, 255))

        verde = Color("Verde", (0, 255, 0))
        verdeClaro = Color("VerdeClaro", (0, 255, 127))
        celeste = Color("Celeste", (0, 255, 255))

        vino = Color("Vino", (127, 0, 0))
        morado = Color("Morado", (127, 0, 127))
        purpura = Color("Purpura", (127, 0, 255))

        amarilloVerdoso = Color("AmarilloVerdoso", (127, 127, 0))
        gris = Color("Gris", (127, 127, 127))
        lila = Color("Lila", (127, 127, 255))

        lima = Color("Lima", (127, 255, 0))
        limaClaro = Color("LimaClaro", (127, 255, 127))
        celesteClaro = Color("CelesteClaro", (127, 255, 255))

        rojo = Color("Rojo", (255, 0, 0))
        fucsia = Color("Fucsia", (255, 0, 127))
        rosado = Color("Rosado", (255, 0, 255))

        naranja = Color("Naranja", (255, 127, 0))
        paloRosa = Color("PaloRosa", (255, 127, 127))
        pink = Color("Pink", (255, 127, 255))

        amarillo = Color("Amarillo", (255, 255, 0))
        amarilloClaro = Color("AmarilloClaro", (255, 255, 127))
        blanco = Color("Blanco", (255, 255, 255))
        return [negro, azulOscuro, azul, verdeOscuro, turquesaOscuro, azulClaro, verde, verdeClaro, celeste, vino,
                   morado,
                   purpura, amarilloVerdoso, gris, lila, lima, limaClaro, celesteClaro, rojo, fucsia, rosado, naranja,
                   paloRosa, pink, amarillo,
                   amarilloClaro, blanco]
