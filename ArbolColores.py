"""from Color import *
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

colores = [negro, azulOscuro, azul, verdeOscuro, turquesaOscuro, azulClaro, verde, verdeClaro, celeste, vino, morado,
           purpura]
colores = colores + [gris, lila, lima, limaClaro, celesteClaro, rojo, fucsia, rosado, naranja, paloRosa, pink, amarillo,
                     amarilloClaro, blanco]


def armarArbolColores(colorR):
    arbolR = Node(colorR)
    verdeIndex = 0
    for colorVerde in range(0, 3):
        colorVerde = 'verde' + str(int(verdeIndex))
        colorVerde = Node(colorVerde, parent=arbolR)
        azulIndex = 0
        for colorAzul in range(0, 3):
            colorAzul = 'azul' + str(int(azulIndex))
            colorAzul = Node(colorAzul, parent=colorVerde)
            azulIndex += 127.5
        verdeIndex += 127.5

    return arbolR


def llenarArbol(colores):
    for color in colores:
        if color.rgb[0] == 0:
            llenarArbolAux(arbolR0, color)
        if color.rgb[0] == 127:
            llenarArbolAux(arbolR127, color)
        if color.rgb[0] == 255:
            llenarArbolAux(arbolR255, color)


def llenarArbolAux(nodo, color):
    if nodo.is_leaf:
        Node(color, parent=nodo, rgb=color.rgb)
    else:
        verdeNodo = "verde" + str(color.rgb[1])
        verdeNodo = find(nodo, lambda node: node.name == verdeNodo)
        azulNodo = 'azul' + str(color.rgb[2])
        azulNodo = find(verdeNodo, lambda node: node.name == azulNodo)
        return llenarArbolAux(azulNodo, color)


def buscarColor(nodo, color):
    return find_by_attr(nodo, name="rgb", value=color).name

arbolR0 = armarArbolColores(0)
arbolR127 = armarArbolColores(127)
arbolR255 = armarArbolColores(255)
llenarArbol(colores)

"""