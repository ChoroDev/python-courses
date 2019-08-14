# 9 вариант
firstFile = 'dz4/f1.txt'
secondFile = 'dz4/f2.txt'
chunk_size = 1<<13


firstFileLen = 0
with open(firstFile, 'r') as filedesc:
    firstFileLen = sum(chunk.count('\n') for chunk in iter(lambda: filedesc.read(chunk_size), ''))

    
n1 = int(input('Enter first string (0-{0}): '.format(firstFileLen)))
if n1 < 0 or n1 > firstFileLen:
    print('error: wrong bound')
    exit()
n2 = int(input('Enter last string (0-{0}): '.format(firstFileLen)))
if n2 < 0 or n2 > firstFileLen:
    print('error: wrong bound')
    exit()
if n2 < n1:
    print('error: bound 1 must be less than bound 2')
    exit()


stringsWithA = []
i = 0
for line in open(firstFile, 'r'):
    i += 1
    if i <= n1:
        continue
    if i >= n2:
        break
    if line[0] == 'A':
        stringsWithA.append(line)


with open(secondFile, 'w') as filedesc:
    filedesc.writelines(stringsWithA)


with open(secondFile, 'r') as filedesc:
    firstStringWordsCount = len(filedesc.readline().split())
    print('First string in second file has {0} word(s)'.format(firstStringWordsCount))