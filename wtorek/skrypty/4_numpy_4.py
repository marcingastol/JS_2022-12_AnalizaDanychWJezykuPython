import numpy as np

a = np.ones((10,6))

for x in range(10):
    a[x] = x

#print(a)

#print(a[[-1,-3]])

b = np.arange(56).reshape(8,7)
#print(b)
# transpose tablic
#print(b.T)

#############################################################

c = np.array([[34,56],[67,89],[23,45],[67,26],[56,68]])

print(c)
print(c.T)
print(np.dot(c.T, c))

print(c.T @ c)

print(c.swapaxes(0,1))