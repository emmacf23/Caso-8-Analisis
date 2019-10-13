from Color import Color

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

from collections import deque


class Arbol:
    def __init__(self, elemento):
        self.elemento = elemento
        self.hijos = []


def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))


def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        encontrado = buscarSubarbol(subarbol, elemento)
        if encontrado != None:
            return encontrado
    return None  # Exceptions


def buscarElemento(arbol, elemento):
    if type(arbol.elemento) == Color:
        if arbol.elemento.rgb == elemento:
            return elemento
    if arbol.elemento == elemento:
        return elemento
    for subarbol in arbol.hijos:
        encontrado = buscarSubarbol(subarbol, elemento)
        if encontrado != None:
            return encontrado.elemento
    return None  # Exceptions


def profundidad(arbol):
    if len(arbol.hijos) == 0:
        return 1
    profundidades = map(profundidad, arbol.hijos)
    return 1 + max(profundidades)


#
# RECORRIDOS
#

def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)


def ejecutarAnchoPrimero(arbol, funcion, cola=deque()):
    funcion(arbol.elemento)
    if (len(arbol.hijos) > 0):
        cola.extend(arbol.hijos)
    if (len(cola) != 0):
        ejecutarAnchoPrimero(cola.popleft(), funcion, cola)


def printElement(element):
    print(element)


inicio = "Inicio"
r0 = "R0"
r127 = "R127"
r255 = "R255"

R0G0 = "R: 0 G: 0"
R0G127 = "R: 0 G: 127"
R0G255 = "R: 0 G:255"

R127G0 = "R:127G: 0"
R127G127 = "R:127 G:127"
R127G255 = "R:127 G:255"

R255G0 = "R:255 G:0"
R255G127 = "R:255 G: 127"
R255G255 = "R:255 G:255"

arbol = Arbol(inicio)

agregarElemento(arbol, r0, inicio)
agregarElemento(arbol, r127, inicio)
agregarElemento(arbol, r255, inicio)

"G"
agregarElemento(arbol, R0G0, r0)
agregarElemento(arbol, R0G127, r0)
agregarElemento(arbol, R0G255, r0)

agregarElemento(arbol, R127G0, r127)
agregarElemento(arbol, R127G127, r127)
agregarElemento(arbol, R127G255, r127)

agregarElemento(arbol, R255G0, r255)
agregarElemento(arbol, R255G127, r255)
agregarElemento(arbol, R255G255, r255)

"B"

agregarElemento(arbol, negro, R0G0)
agregarElemento(arbol, azulOscuro, R0G0)
agregarElemento(arbol, azul, R0G0)

agregarElemento(arbol, verdeOscuro, R0G127)
agregarElemento(arbol, turquesaOscuro, R0G127)
agregarElemento(arbol, azulClaro, R0G127)

agregarElemento(arbol, verde, R0G255)
agregarElemento(arbol, verdeClaro, R0G255)
agregarElemento(arbol, celeste, R0G255)

"B"
agregarElemento(arbol, vino, R127G0)
agregarElemento(arbol, morado, R127G0)
agregarElemento(arbol, purpura, R127G0)

agregarElemento(arbol, amarilloVerdoso, R127G127)
agregarElemento(arbol, gris, R127G127)
agregarElemento(arbol, lila, R127G127)

agregarElemento(arbol, lima, R127G255)
agregarElemento(arbol, limaClaro, R127G255)
agregarElemento(arbol, celesteClaro, R127G255)

"b"
agregarElemento(arbol, rojo, R255G0)
agregarElemento(arbol, fucsia, R255G0)
agregarElemento(arbol, rosado, R255G0)

agregarElemento(arbol, naranja, R255G127)
agregarElemento(arbol, paloRosa, R255G127)
agregarElemento(arbol, pink, R255G127)

agregarElemento(arbol, amarillo, R255G255)
agregarElemento(arbol, amarilloClaro, R255G255)
agregarElemento(arbol, blanco, R255G255)

# print(profundidad(arbol))

#
# PROFUNDIDAD
#

# ejecutarProfundidadPrimero(arbol, printElement)
print(buscarElemento(arbol, (255,127,127)))
