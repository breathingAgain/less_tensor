#!/usr/bin/env python
import os


def moleculs(odds):
    count = 0
    while True:
        if (odds[0] // 2 != 0 and odds[1] // 6 != 0 and odds[2] // 1 != 0):
            odds[0] -= 2
            odds[1] -= 6
            odds[2] -= 1
            count += 1
        else:
            break
    return str(count)


file = str(input("Введите название файла: "))  # Input.txt; первая строка - C
# вторая строка - O, третья строка - H
if os.path.exists(file):
    f = open(file, 'r')
else:
    print('Нет такого файла')
    exit(0)

lines = f.readlines()
f.close
odds = [int(x) for x in lines]
f = open('Output.txt', 'w')
rec = 'number of molecules: ' + moleculs(odds)
f.write(rec)
f.close





