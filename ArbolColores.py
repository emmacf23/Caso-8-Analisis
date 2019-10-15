
class Node:
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
            nodoRojo = Node('Rojo', int(rojoIndex))
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

    def addColor(self, color, colorActual):
        if self.is_leaf():
            self.add_child(color)
        else:
            if colorActual[0] <= 85:
                self.children[0].addColor(color, colorActual[1:])
            elif colorActual[0] >= 86 and colorActual[0] <= 170:
                self.children[1].addColor(color, colorActual[1:])
            else:
                self.children[2].addColor(color, colorActual[1:])

    def fillColors(self, colores):
        for color in colores:
            self.addColor(color, color.rgb)

    def searchColor(self, color):
        if len(self.children) == 1:
            return self.children[0]
        else:
            if color[0] <= 85:
                return self.children[0].searchColor(color[1:])
            elif color[0] >= 86 and color[0] <= 170:
                return self.children[1].searchColor(color[1:])
            else:
                return self.children[2].searchColor(color[1:])


"""
arbolColores = Node('ArbolColores',0)
arbolColores.armarArbolColores()
arbolColores.fillColors(colores)
"""
