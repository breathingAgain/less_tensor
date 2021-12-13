#!/usr/bin/env python
"""Соортировка списка пузырьком"""
a = [4, 6, 67, 5, 89, 
     0, 23, 12, 89, 9]
print(a)
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            buff = a[j]
            a[j] = a[j+1]
            a[j+1] = buff

print(a)
