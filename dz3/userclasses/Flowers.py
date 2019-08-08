from userclasses.Shipment import Shipment

class Flowers(Shipment):
    __colour = 'None'


    def __init__(self, count, unitPrice, colour):
        super(Flowers, self).__init__('Flowers', 'Non-food', count, unitPrice)
        self.__colour = colour


    def setColour(self, colour):
        if colour:
            self.__colour = colour
        else:
            self.__colour = 'None'


    def getColour(self):
        return self.__colour