import Pixel
from Pixel import *
from Color import *
from anytree import *

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


def armarArbolColores(colorR):
    arbolR = Node(colorR)
    verdeIndex = 0
    for color in range(0, 3):
        verde = 'verde' + str(verdeIndex)
        verde = Node(verde, parent=arbolR)
        azulIndex = 0
        for colorcillo in range(0, 3):
            azul = 'azul' + str(azulIndex)
            azul = Node(azul, parent=verde)
            azulIndex += 127
        verdeIndex += 127

    return arbolR


arbolR0 = armarArbolColores(0)
Node(negro, parent=arbolR0.children[0].children[0])
Node(azulOscuro, parent=arbolR0.children[0].children[1])
Node(azul, parent=arbolR0.children[0].children[2])

Node(verdeOscuro, parent=arbolR0.children[1].children[0])
Node(turquesaOscuro, parent=arbolR0.children[1].children[1])
Node(azulClaro, parent=arbolR0.children[1].children[2])

Node(verde, parent=arbolR0.children[2].children[0])
Node(verdeClaro, parent=arbolR0.children[2].children[1])
Node(celeste, parent=arbolR0.children[2].children[2])

arbolR127 = armarArbolColores(127)
Node(vino, parent=arbolR127.children[0].children[0])
Node(morado, parent=arbolR127.children[0].children[1])
Node(purpura, parent=arbolR127.children[0].children[2])

Node(amarilloVerdoso, parent=arbolR127.children[1].children[0])
Node(gris, parent=arbolR127.children[1].children[1])
Node(lila, parent=arbolR127.children[1].children[2])

Node(lima, parent=arbolR127.children[2].children[0])
Node(limaClaro, parent=arbolR127.children[2].children[1])
Node(celesteClaro, parent=arbolR127.children[2].children[2])

arbolR255 = armarArbolColores(255)
Node(rojo, parent=arbolR255.children[0].children[0])
Node(fucsia, parent=arbolR255.children[0].children[1])
Node(rosado, parent=arbolR255.children[0].children[2])

Node(naranja, parent=arbolR255.children[1].children[0])
Node(paloRosa, parent=arbolR255.children[1].children[1])
Node(pink, parent=arbolR255.children[1].children[2])

Node(amarillo, parent=arbolR255.children[2].children[0])
Node(amarilloClaro, parent=arbolR255.children[2].children[1])
Node(blanco, parent=arbolR255.children[2].children[2])


def buscarColor(color):
    if color.rgb[0] > 127:
        findall(arbolR255.root, filter_=lambda node: node.name in color)


"""
def buscarColor(nodo, color):
    # def temp_multi_search(some_node, key):
    result = []  # Line 1
    if nodo.val == color:
        print('found', nodo)
        result.append(nodo)  # Line 2
    for subtree in nodo.subtrees:
        result.extend(buscarColor(subtree, color))  # Line 3
    return result
"""


class Sector:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.listPixels = []
        self.porcentageColor = 0.0
        self.probability = 1.0
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.matrizColores = [[negro, azul, verde, celeste, rojo, morado, amarillo], [0, 0, 0, 0, 0, 0, 0]]
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

    def aumentarNegros(self):
        self.matrizColores[1][0] += 1

    def aumentarAzules(self):
        self.matrizColores[1][1] += 1

    def aumentarVerde(self):
        self.matrizColores[1][2] += 1

    def aumentarCeleste(self):
        self.matrizColores[1][3] += 1

    def aumentarRojo(self):
        self.matrizColores[1][4] += 1

    def aumentarMorado(self):
        self.matrizColores[1][5] += 1

    def aumentarAmarillo(self):
        self.matrizColores[1][6] += 1
