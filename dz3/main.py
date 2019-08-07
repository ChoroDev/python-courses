# variant 9 task 1
from datetime import timedelta

class Phone:
    _maxId = 0
    _initialSurname = 'Doe'
    _initialName = 'John'
    _initialPatronymic = 'Victorovich'

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
        self.__patronymic = patronymic


    def setAddress(self, address):
        self.__address = address


    def setAccount(self, account):
        self.__account = account


    def setDebit(self, debit):
        self.__debit = debit


    def setCredit(self, credit):
        self.__credit = credit


    def setCityCallsTime(self, cityCallsTime):
        self.__cityCallsTime = cityCallsTime


    def setLongDistanceCallsTime(self, longDistanceCallsTime):
        self.__longDistanceCallsTime = longDistanceCallsTime


    def __init__(self):
        self.setId(0)
        self.setSurname(Phone._initialSurname)
        self.setName(Phone._initialName)
        self.setPatronymic(Phone._initialPatronymic)
        self.setAddress('LA')
        self.setAccount('0000-0000-0000-0000')
        self.setDebit(0)
        self.setCredit(0)
        self.setCityCallsTime(0)
        self.setLongDistanceCallsTime(0)


class PredefinedPhone(Phone):
    def __init__(self, id, surname, name, patronymic, address, account, debit, credit, cityCallsTime, longDistanceCallsTime):
        self.__id = id
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__address = address
        self.__account = account
        self.__debit = debit
        self.__credit = credit
        self.__cityCallsTime = cityCallsTime
        self.__longDistanceCallsTime = longDistanceCallsTime