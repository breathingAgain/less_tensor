#!/usr/bin/env python
import random
a = set()
b = set()
for i in range(0,15):
    a.add(random.randint(0,100))
    b.add(random.randint(0,100))
print(a)
print(b)

inp = a & b #Obedinenie
print(inp)

inp = a - b #pervoe, no bez vtorogo
print(inp)

inp = b - a #vtoroe, no bez pervogo
print(inp)

inp = a ^ b #ne povtoryayushiesya v oboih
print(inp)