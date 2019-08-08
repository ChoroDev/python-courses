# variant 9 task 1
from datetime import timedelta
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


class PredefinedPhone(Phone):
    def __init__(self, id = 0, surname = Phone._initialSurname, name = Phone._initialName, patronymic = Phone._initialPatronymic, address = Phone._initialAddress, account = Phone._initialAccount, debit = 0, credit = 0, cityCallsTime = 0, longDistanceCallsTime = 0):
        self.setId(id)
        self.setSurname(surname)
        self.setName(name)
        self.setPatronymic(patronymic)
        self.setAddress(address)
        self.setAccount(account)
        self.setDebit(debit)
        self.setCredit(credit)
        self.setCityCallsTime(cityCallsTime)
        self.setLongDistanceCallsTime(longDistanceCallsTime)
        print('"PredefinedPhone" constructor processed')


phoneList = [ 
    Phone(), 
    PredefinedPhone(account = '0000-0000-0000-0001', cityCallsTime = 10001, longDistanceCallsTime = 10), 
    PredefinedPhone(account = '0000-0000-0000-0002', cityCallsTime = 12), 
    PredefinedPhone(account = '0000-0000-0000-0003', cityCallsTime = 133, longDistanceCallsTime = 100) 
    ]

for phone in phoneList:
    if phone.isCityCallsTimeExceeded():
        print('Phone with id = ', phone.getId(), ': city calls time exceeded')
    if phone.isLongDistanceCallsUsed():
        print('Phone with id = ', phone.getId(), ': long distance calls used')