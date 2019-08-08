class Product:
    _defaultName = 'Thing'
    _defaultType = 'None'
    _name = ''
    _type = ''


    def __init__(self, name, type):
        self.setName(name)
        self.setType(type)

    
    def setName(self, name):
        if name:
            self._name = name
        else:
            print('Warning: name is empty, setting ' + Product._defaultName + ' instead')
            self._name = Product._defaultName


    def getName(self):
        return self._name


    def setType(self, type):
        if type:
            self._type = type
        else:
            self._type = Product._defaultType


    def getType(self):
        return self._type