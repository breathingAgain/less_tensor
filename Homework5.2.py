#!/usr/bin/env python
def Sum_i(*args):
    sum = 0
    for i in args:
        sum += i
    
    return sum

print ('Cумма цифр от 1 до 8 =', Sum_i(1,2,3,4,5,6,7,8))
