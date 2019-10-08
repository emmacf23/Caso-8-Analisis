class Color:
    def __init__(self, nombre, rgb):
        self.nombre = nombre
        self.rgb = rgb
        self.porcentage = 0
        self.cantidad = 0

    def __repr__(self):
        return '{}: {} {} {} {}'.format(self.__class__.__name__,
                                        self.nombre,
                                        self.rgb)
