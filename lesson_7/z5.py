import numpy as np

m = np.empty((3,3), dtype='int8')
print('Сгенерированная матрица:')
print(m)

t = np.transpose(m)
print('Транспонированная матрица:')
print(t)