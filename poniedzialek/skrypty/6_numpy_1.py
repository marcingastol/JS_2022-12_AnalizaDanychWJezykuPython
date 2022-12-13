import numpy as np
import datetime as dt

start1 = dt.datetime.now()
tablica1 = np.arange(100_000_000)
start2 = dt.datetime.now()
tablica2 = list(range(100_000_000))
start3 = dt.datetime.now()

print(start2 - start1)
print(start3 - start2)