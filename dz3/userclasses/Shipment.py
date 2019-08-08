from userclasses.Product import Product

class Shipment(Product):
    def __init__(self, name = '', type = '', count = 0, unitPrice = 0):
        super(Shipment, self).__init__(name, type)
        self.setCount(count)
        self.setUnitPrice(unitPrice)


    def setCount(self, count):
        if count < 0:
            print('Error: count must be 0 or positive')
        else:
            self.__count = count


    def getCount(self):
        return self.__count


    def setUnitPrice(self, unitPrice):
        if unitPrice < 0:
            print('Error: unit price must be 0 or positive')
        else:
            self.__unitPrice = unitPrice

    
    def getUnitPrice(self):
        return self.__unitPrice