#!/usr/bin/env python
"""Работа с матрицами, модулем numpy"""
import numpy as np
matrix = np.random.randint(0,30, size=(3,3))
print('Матрица: \n',matrix)
matrix_t = matrix.transpose()
print('Транспонированная матрица:\n', matrix_t)
