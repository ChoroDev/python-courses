from userclasses.Shipment import Shipment

class Watch(Shipment):
    __producingCountry = 'None'


    def __init__(self, count, unitPrice, producingCountry):
        super(Watch, self).__init__('Watch', 'Non-food', count, unitPrice)
        self.__producingCountry = producingCountry


    def setProducingCountry(self, producingCountry):
        if producingCountry:
            self.__producingCountry = producingCountry
        else:
            self.__producingCountry = 'None'


    def getProducingCountry(self):
        return self.__producingCountry