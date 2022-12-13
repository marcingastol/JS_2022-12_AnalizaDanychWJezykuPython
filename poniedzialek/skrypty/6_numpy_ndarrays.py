import numpy as np

a = np.array([[5156,1658,266,13165.8],[-54,651,65,6],[153,-65,13,-65]])
#print(a * 100)

#print(a.shape)
#print(a.dtype)
#print(type(a))
#print(a.ndim)

b = np.zeros((5,7))
#print(b)

c = np.empty((5,7))
#print(c)

c = np.ones((5,7))
#print(c.dtype)

d = np.array([23324,234,23546.5656,6789,123.435], dtype=np.int32)
print(d)
print(d.dtype)

e = d.astype(np.float64)
print(e)
print(e.dtype)

f = np.array(["23324",234,"23546.5656",6789,123.435])
print(f.dtype)

g = f.astype(np.float64).astype(np.int32)
print(g)