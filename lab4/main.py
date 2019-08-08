from sklearn.datasets import load_iris
import os

def first():
    filename = input('Enter filename: ')
    if filename[-3:0] != 'csv':
        filename += '.csv'

    iris_dataset = load_iris()
    header = ''
    for i in iris_dataset['feature_names']:
        header += i + ';'
        header += 'Target'


    with open(filename, 'w') as filedesc:
        filedesc.write(header + '\n')
        for i in range(len(iris_dataset['data'])):
            line = ''
            for j in iris_dataset['data'][i]:
                line += str(j).replace('.', ',') + ';'
            line += str(iris_dataset['target'][i])
            filedesc.write(line + '\n')

    os.startfile(filename)


class Iris:
    def __init__(self, **info):
        if 'data' in info and 'target' in info:
            self.sepal_length = info['data'][0]
            self.sepal_width = info['data'][1]
            self.petal_length = info['data'][2]
            self.petal_width = info['data'][3]
            self.target = info['target']
        elif 'data_and_target' in info:
            self.sepal_length = float(info['data_and_target'][0])
            self.sepal_width = float(info['data_and_target'][1])
            self.petal_length = float(info['data_and_target'][2])
            self.petal_width = float(info['data_and_target'][3])
            self.target = int(info['data_and_target'][4])
    
iris_list = []

filename = input('Enter filename: \n')

if filename == '0':
    iris_datasets = load_iris()

    for i in range(len(iris_datasets['data'])):
        iris_list.append(Iris(data = iris_datasets['data'], target = iris_datasets['target'][i]))
else:
    if filename[-3:0] != 'csv':
        filename += '.csv'
    with open(filename, 'r') as filedesc:
        filecontent = filedesc.readlines()
        for i in range(len(filecontent)):
            if i > 0:
                cells = filecontent[i].split(';')
                iris_list.append(Iris(data_and_target = cells))

field_num = int(input('Enter filter field: \n0 - do not filter\n1 - sepal length\n2 - sepal width\n3 - petal length\n4 - petal width\n5 - target\n'))
filtered_list = []
if field_num == 0:
    filtered_list = iris_list.copy()
else:
    min_num = float(input('Enter min possible value: '))
    max_num = float(input('Enter max possible value: '))

    if filtered_list == 1:
        for i in iris_list:
            if min_num <= i.sepal_length <= max_num:
                filtered_list.append(i)
    elif filtered_list == 2:
        for i in iris_list:
            if min_num <= i.sepal_width <= max_num:
                filtered_list.append(i)
    elif filtered_list == 3:
        for i in iris_list:
            if min_num <= i.petal_length <= max_num:
                filtered_list.append(i)
    elif filtered_list == 4:
        for i in iris_list:
            if min_num <= i.petal_width <= max_num:
                filtered_list.append(i)
    elif filtered_list == 5:
        for i in iris_list:
            if min_num <= i.target <= max_num:
                filtered_list.append(i)


filename = input('Enter data to save: ')
if filename[-3:0] != 'csv':
    filename += '.csv'
header = 'sepal length (cm);sepal width (cm);petal length (cm);petal width (cm);target'
with open(filename, 'w') as filedesc:
    filedesc.write(header + '\n')
    for i in filtered_list:
        line = str(i.sepal_length) + ';' + str(i.sepal_width) + ';' + str(i.petal_length) + ';' + str(i.petal_width) + ';' + str(i.target)
        filedesc.write(line.replace('.', ',') + '\n')

os.startfile(filename)