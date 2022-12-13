import numpy as np

a = np.random.randint(1,30,(5,6))
b = np.random.randint(1,30,(5,6))

print(a)
print(b)

#print(np.sqrt(a))
#print(np.exp(a))
#print(np.minimum(a,b))

np.add(a, 5, out=b)

print(b)