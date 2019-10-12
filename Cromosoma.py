class Cromosoma:
    def __init__(self, pGenes, pPoint1, pPoint2, pPoint3, pPoint4, pColor):
        self.genes = pGenes
        self.aptitud = 0
        self.point1 = pPoint1
        self.point2 = pPoint2
        self.point3 = pPoint3
        self.point4 = pPoint4
        self.Color = pColor

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                        self.genes,
                                        self.Color)