import pandas as pd
import numpy as np

##################################################
# 1. Porównaj elementy dwóch serii ze sobą : >, <, ==

a = pd.Series([1,2,3,4,5])
b = pd.Series([4,2,3,5,2])

print(a == b)
print(a > b)
print(a < b)

print(id(a))
print(id(b))