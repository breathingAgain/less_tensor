#!/usr/bin/env python
def transform_en(str):
    """Кодировка списка строк"""
    for i in range(len(str)):
        str[i] = str[i].encode('utf-8')
    return str


def transform_de(str):
    """Декодирование списка байтов"""
    for i in range(len(str)):
        str[i] = str[i].decode('utf-8')
    return str


str = ['а', 'б', 'в']
b = [b'\xd0\xb0', b'\xd0\xb1', b'\xd0\xb2']
print('Закодированный список строк', transform_en(str))
print('Декодированный список байтов', transform_de(b))
