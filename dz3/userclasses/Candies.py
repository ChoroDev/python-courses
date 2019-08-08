from userclasses.Shipment import Shipment

class Candies(Shipment):
    __firm = 'None'


    def __init__(self, count, unitPrice, firm):
        super(Candies, self).__init__('Candies', 'Food', count, unitPrice)
        self.__firm = firm


    def setFirm(self, firm):
        if firm:
            self.__firm = firm
        else:
            self.__firm = 'None'


    def getFirm(self):
        return self.__firm