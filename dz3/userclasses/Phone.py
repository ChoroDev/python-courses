import re

class Phone:
    _maxId = 0
    _initialSurname = 'Doe'
    _initialName = 'John'
    _initialPatronymic = 'Victorovich'
    _initialAddress = 'LA'
    _initialAccount = '0000-0000-0000-0000'
    _pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    _maxCityCallsTime = 10000

    __id = 0
    __surname = ''
    __name = ''
    __patronymic = ''
    __address = ''
    __account = ''
    __debit = 0
    __credit = 0
    __cityCallsTime = 0
    __longDistanceCallsTime = 0
    

    def __init__(self):
        self.setId(0)
        self.setSurname(Phone._initialSurname)
        self.setName(Phone._initialName)
        self.setPatronymic(Phone._initialPatronymic)
        self.setAddress(Phone._initialAddress)
        self.setAccount(Phone._initialAccount)
        self.setDebit(0)
        self.setCredit(0)
        self.setCityCallsTime(0)
        self.setLongDistanceCallsTime(0)
        print('"Phone" constructor processed')


    def __del__(self):
        print('"Phone" object deleted')

    
    def setId(self, id):
        if id > Phone._maxId:
            self.__id = id
        elif id == 0:
            self.__id = Phone._maxId + 1
            Phone._maxId += 1


    def getId(self):
        return self.__id


    def setSurname(self, surname):
        if surname:
            self.__surname = surname
        else:
            print('Warning: surname is empty, setting "', Phone._initialSurname, '" instead')
            self.__surname = Phone._initialSurname

    
    def getSurname(self):
        return self.__surname


    def setName(self, name):
        if name:
            self.__name = name
        else:
            print('Warning: name is empty, setting "', Phone._initialName, '" instead')
            self.__name = Phone._initialName


    def getName(self):
        return self.__name


    def setPatronymic(self, patronymic):
        if patronymic:
            self.__patronymic = patronymic
        else:
            print('Warning: patronymic is empty, setting "', Phone._initialPatronymic, '" instead')
            self.__patronymic = Phone._initialPatronymic


    def getPatronymic(self):
        return self.__patronymic


    def setAddress(self, address):
        if address:
            self.__address = address
        else:
            print('Warning: address is empty, setting "', Phone._initialAddress, '" instead')
            self.__address = Phone._initialAddress


    def getAddress(self):
        return self.__address


    def setAccount(self, account):
        if re.fullmatch(Phone._pattern, account):
            self.__account = account
        else:
            print('Error: account must match the pattern xxxx-xxxx-xxxx-xxxx, where x is digit')


    def getAccount(self):
        return self.__account


    def setDebit(self, debit):
        if debit >= 0:
            self.__debit = debit
        else:
            print('Error: debit must be >= 0')


    def getDebit(self):
        return self.__debit


    def setCredit(self, credit):
        if credit >= 0:
            self.__credit = credit
        else:
            print('Error: credit must be >= 0')


    def getCredit(self):
        return self.__credit


    def setCityCallsTime(self, cityCallsTime):
        if cityCallsTime >= 0:
            self.__cityCallsTime = cityCallsTime
        else:
            print('Error: city calls time must be >= 0')


    def getCityCallsTime(self):
        return self.__cityCallsTime


    def setLongDistanceCallsTime(self, longDistanceCallsTime):
        if longDistanceCallsTime >= 0:
            self.__longDistanceCallsTime = longDistanceCallsTime
        else:
            print('Error: long distance calls time must be >= 0')


    def getLongDistanceCallsTime(self):
        return self.__longDistanceCallsTime


    def isCityCallsTimeExceeded(self):
        if self.__cityCallsTime > Phone._maxCityCallsTime:
            return True
        else:
            return False


    def isLongDistanceCallsUsed(self):
        if self.__longDistanceCallsTime > 0:
            return True
        else:
            return False