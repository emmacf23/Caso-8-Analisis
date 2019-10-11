from Color import *


class Rango:
    def __init__(self, color, cromosomaMinimo, cromosomaMaximo):
        self.color = color
        self.porcentage = color.porcentage
        self.cromosomaMinimo = cromosomaMinimo
        self.cromosomaMaximo = cromosomaMaximo

    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                        self.color,
                                        self.cromosomaMinimo,
                                        self.cromosomaMaximo)
