# variant 9
from userclasses.Phone import Phone
from userclasses.PredefinedPhone import PredefinedPhone
from userclasses.Cake import Cake
from userclasses.Watch import Watch
from userclasses.Candies import Candies
from userclasses.Flowers import Flowers
from userclasses.Shipment import Shipment


phoneList = [ 
    Phone(), 
    PredefinedPhone(account = '0000-0000-0000-0001', cityCallsTime = 10001, longDistanceCallsTime = 10), 
    PredefinedPhone(account = '0000-0000-0000-0002', cityCallsTime = 12), 
    PredefinedPhone(account = '0000-0000-0000-0003', cityCallsTime = 133, longDistanceCallsTime = 100) 
]

for phone in phoneList:
    setattr(phone, '__isInCity ', False)
    setattr(phone, '__hasNonCityLinks', False)
    if phone.isCityCallsTimeExceeded():
        print('Phone with id = ', phone.getId(), ': city calls time exceeded')
        setattr(phone, '__isInCity ', True)
    if phone.isLongDistanceCallsUsed():
        print('Phone with id = ', phone.getId(), ': long distance calls used')
        setattr(phone, '__hasNonCityLinks', True)
        setattr(phone, '__isInCity', False)
    else:
        setattr(phone, '__hasNonCityLinks', False)


shipment = [
    Flowers(10, 5, 'Blue'),
    Candies(100, 1, 'Roshen'),
    Watch(5, 200, 'Switzerland'),
    Cake(3, 20, 'Big'),
    Shipment(type = 'Food', count = 3, unitPrice = 10)
]

for thing in shipment:
    if thing.getName() == 'Thing':
        print('You have to delete that "Thing" from your shop')