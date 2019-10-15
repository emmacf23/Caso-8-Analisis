class Imagen:
    def __init__(self, name, sectores):
        self.name = name
        self.sectores = sectores

    def __repr__(self):
        return '{}: {} {} '.format(self.__class__.__name__,
                                     self.name,
                                     self.sectores, )
