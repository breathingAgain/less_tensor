#!/usr/bin/env python
import re
print('Введите пароль: ')
passw = input()
if len(passw) < 6: 
    print('Длинна пароля меньше 6')
    exit(0)

if passw.isdigit() == True:
    print('Пароль состоит только из цифр')
    exit(0)

if re.search('\d+', passw) == None:
   print('В пароле нет цифр')
   exit(0)

bad_passw = 'password'
user_passw = passw.lower()
if re.search(bad_passw, user_passw) != None:
    print('Пароль содержит плохое слово "password"')
    exit(0)

print('Пароль хороший!')

