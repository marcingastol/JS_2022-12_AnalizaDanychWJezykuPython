import numpy as np

#######################################
# 1. Stwórz tablicę 20-elementową z wartościami 10


a = np.ones(20) * 10
print(a)

#######################################
# 2. Stwórz tablicę 4wierszową i 5kolumnowa z losowymi liczbami całkowitymi w przedziale 1-100 (podpowiedź: użyj metody random z numpy)

b = np.random.randint(1,100, (4,5))
print(b)

#######################################
# 3. Stwórz tablicę 5x5 posiadającą wszystkie wartości jako NaN (podpowiedź: użyj typu danych np.nan)

c = np.ones((5,5))
c[:] = np.nan
print(c)