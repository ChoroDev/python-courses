class Table:
    #region Fields

    __mass = 0

    #endregion


    #region Public methods

    def __init__(self, mass_):
        self.__mass = mass_

    def get_mass(self):
        return self.__mass

    #endregion


class DinnerTable(Table):
    __places = 0

    def __init__(self, mass1):
        Table.__init__(self, mass1)
        self.__places = mass1 // 5

    def get_places(self):
        return self.__places


class Truck:
    __maxMass = 0

    def __init__(self, max_mass):
        self.__maxMass = max_mass

        self.__tables = []

    
    def __current_mass(self):
        s = 0
        for i in self.__tables:
            s += i.get_mass()
        return s


    def reserved_mass(self):
        return self.__maxMass - self.__current_mass()


    def add_table(self, new_table):
        if new_table.get_mass() < self.reserved_mass():
            self.__tables.append(new_table)
            print('Table with mass = {0} is loaded'.format(new_table.get_mass()))
        else:
            print('Table with mass = {0} is not loaded. Only {1} unit(s) left'.format(new_table.get_mass(), self.reserved_mass()))


    def tables_to_string(self, num):
        s = str(num)
        last_s = s[-1:]

        if 10 <= num <= 20:
            return 'столов'

        elif last_s == '1':
            return 'стол'

        elif last_s == '2' or last_s == '3' or last_s == '4':
            return 'стола'

        else:
            return 'столов'

    def count_by_mass(self, needle, selector):
        s = 0
        for i in self.__tables:
            if selector(i) == needle:
                se+= 1
        return s


    def remove_tables(self):
        self.__tables.clear()


    def get_max_mass(self):
        return self.__maxMass


newTables = [
    DinnerTable(10),
    DinnerTable(20),
    DinnerTable(30)
]


newTrucks = [ Truck(50), Truck(60) ] 
need = [ 3, 3 ]

while True:
    select = 0
    sums = list([])
    sums.append(
        newTrucks[0].count_by_mass(newTables[0].get_mass(), Table.get_mass) + 
        newTrucks[1].count_by_mass(newTables[0].get_mass(), Table.get_mass)
    )

    sums.append(
        newTrucks[0].count_by_mass(newTables[1].get_mass(), Table.get_mass) + 
        newTrucks[1].count_by_mass(newTables[1].get_mass(), Table.get_mass)
    )

    if sums[0] == need[0] and sums[1] == need[1]:
        print('Congratulations, trucks are loaded!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        break

    while True:
        print('There are two trucks with capacity: {0} and {1} units'.format(newTrucks[0].get_max_mass(), newTrucks[1].get_max_mass()))
        print('Needed {0} {1} with {2} units and {3} {4} with {5} units'.format(
            need[0], 
            newTrucks[0].tables_to_string(need[0]), 
            newTables[0].get_mass(), 
            need[1],
            newTrucks[1].tables_to_string(need[1]),
            newTables[1].get_mass()
            )
        )
        print('Loaded: {0} {1} with {2} units and {3} {4} with {5} units'.format(
            sums[0],
            newTrucks[0].tables_to_string(sums[0]),
            newTables[0].get_mass(),
            sums[1],
            newTrucks[1].tables_to_string(sums[1]),
            newTables[1].get_mass()
            )
        )
        print('What to do: \n',
            '1 - loading table with mass = {0} units in first truck\n'.format(newTables[0].get_mass()),
            '2 - loading table with mass = {0} units in first truck\n'.format(newTables[1].get_mass()),
            '3 - loading table with mass = {0} units in second truck\n'.format(newTables[0].get_mass()),
            '4 - loading table with mass = {0} units in second truck\n'.format(newTables[1].get_mass())
        )

        select = int(input())
        if 1 <= select <= 5:
            break

    if select == 1:
        newTrucks[0].add_table(newTables[0])
    elif select == 2:
        newTrucks[0].add_table(newTables[1])
    elif select == 3:
        newTrucks[1].add_table(newTables[0])
    elif select == 4:
        newTrucks[1].add_table(newTables[1])
    elif select == 5:
        newTrucks[0].remove_tables()
        newTrucks[1].remove_tables()

# newTrucks.add_table(newTable[0])
# newTrucks.add_table(newTable[1])
# newTrucks.add_table(newTable[2])