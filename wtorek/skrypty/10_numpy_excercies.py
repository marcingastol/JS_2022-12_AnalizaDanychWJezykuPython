import numpy as np

############################################
# 1. Stwórz tablicę na podstawie odwrócenia kolejności tablic

a = np.random.randint(1,100,(6,7))
print(a)
print(" ")
print(a[::-1,::-1])

############################################
# 2. Stwórz program, który zwraca liczby większe niż 50 w zadanej tablicy 'a'

#print(a[a > 50])

############################################
# 3. Stwórz program, który zamienia liczby większe niż 50 na wartość 0 w zadanej tablicy 'a'

#print(np.where(a > 50, 0, a))

############################################
# 4. Zwróć informację o istniejących elementach NaN w tablicy jako wartość logiczną

d = np.array([[np.nan, 45, 46],[1, 34,45],[234,np.nan,5],[34,np.nan,np.nan]])
#print(d)
#print(np.isnan(d))