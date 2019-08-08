from userclasses.Shipment import Shipment

class Cake(Shipment):
    __size = 'Medium'


    def __init__(self, count, unitPrice, size):
        super(Cake, self).__init__('Cake', 'Food', count, unitPrice)
        self.__size = size


    def setSize(self, size):
        if size:
            self.__size = size
        else:
            self.__size = 'Medium'


    def getSize(self):
        return self.__size