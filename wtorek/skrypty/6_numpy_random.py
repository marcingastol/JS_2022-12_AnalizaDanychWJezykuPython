import numpy as np

a = np.random.standard_normal((6,7))
#print(a)

b = np.random.default_rng(seed=123)
c = b.standard_normal((6,7))
print(c)