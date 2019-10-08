class Pixel:
    def __init__(self, cordX, cordY, color):
        self.cordX = cordX
        self.cordY = cordY
        self.color = color

    def getCordX(self):
        return self.cordX

    def getCordY(self):
        return self.cordY

    def getColor(self):
        return self.color

    def setCordX(self,cordX):
        self.cordX = cordX

    def setCordY(self,cordY):
        self.cordY = cordY

    def setColor(self,color):
        self.color = color
