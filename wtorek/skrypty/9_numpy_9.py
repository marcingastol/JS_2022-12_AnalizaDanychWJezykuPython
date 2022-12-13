import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
b = np.array([9,8,7,6,5,4,3,2])
c = np.array([True,True,False,True,False,False,True,True])

w = [(x if z else y) for x,y,z in zip(a,b,c)]

#print(w)

w = np.where(c,a,b)
#print(w)

########################################################

d = np.random.randint(-100,100, (5,5))
#print(d)
#print(d > 0)
#print(np.where(d > 0, 1, -1))

########################################################

# sortowanie
d.sort(axis=1)
d.sort(axis=0)
#print(d)

########################################################
# odchylenie standardowe i suma

#print(d.mean(axis=1))
#print(d.sum(axis=1))
#print(d.min(axis=1))
#print(d.max(axis=1))
#print(d.var(axis=1))
#
#print(d)
#print((d < 0).sum())

########################################################
# odczyt/zapis

np.save("numpy", d)
print(np.load("numpy.npy"))

np.savez("numpy2.npz", key1=a, key2=b)
e = np.load("numpy2.npz")
print(e["key1"])
print(e["key2"])

np.savetxt("numpy.txt",d)

# zapis pliku
with open("numpy2.txt", mode="a") as operacje:
    np.savetxt(operacje, a)
    np.savetxt(operacje, b)