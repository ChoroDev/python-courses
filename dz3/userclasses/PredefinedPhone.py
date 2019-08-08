from userclasses.Phone import Phone

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