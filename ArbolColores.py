from Color import *

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

colores = [negro, azulOscuro, azul, verdeOscuro, turquesaOscuro, azulClaro, verde, verdeClaro, celeste, vino, morado,
           purpura]
colores = colores + [gris, lila, lima, limaClaro, celesteClaro, rojo, fucsia, rosado, naranja, paloRosa, pink, amarillo,
                     amarilloClaro, blanco]

class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                     self.name,
                                     self.value,
                                     self.children)

    def add_child(self, obj):
        self.children.append(obj)

    def armarArbolColores(self):
        rojoIndex = 0
        for colorRojo in range(0, 3):
            nodoRojo = Node('Rojo',int(rojoIndex))
            self.add_child(nodoRojo)
            verdeIndex = 0
            for colorVerde in range(0, 3):
                nodoVerde = Node("Verde", int(verdeIndex))
                nodoRojo.add_child(nodoVerde)
                azulIndex = 0
                for colorAzul in range(0, 3):
                    nodoAzul = Node('Azul', int(azulIndex))
                    nodoVerde.add_child(nodoAzul)
                    azulIndex += 127.5
                verdeIndex += 127.5

    def is_leaf(self):
        return len(self.children) == 0

    def addColor(self,color,colorActual):
        if self.is_leaf():
            self.add_child(color)
        else:
            if colorActual[0] <= 85:
                self.children[0].addColor(color,colorActual[1:])
            elif colorActual[0] >= 86 and colorActual[0] <= 170:
                self.children[1].addColor(color,colorActual[1:])
            else:
                self.children[2].addColor(color, colorActual[1:])

    def fillColors(self,colores):
        for color in colores:
            self.addColor(color,color.rgb)

    def searchColor(self,color):
        if len(self.children) == 1:
            return self.children[0]
        else:
            if color[0] <= 85:
                return self.children[0].searchColor(color[1:])
            elif color[0] >= 86 and color[0] <= 170:
                return self.children[1].searchColor(color[1:])
            else:
                return self.children[2].searchColor(color[1:])



arbolColores = Node('ArbolColores',0)
arbolColores.armarArbolColores()
arbolColores.fillColors(colores)