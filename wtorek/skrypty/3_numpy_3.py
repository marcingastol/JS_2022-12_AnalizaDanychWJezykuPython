import numpy as np

a = np.array(["audi","mercedes","bmw","bmw","porsche"])
b = np.array([[34,56],[67,89],[23,45],[67,26],[56,68]])

print(a)
print(b)

#print(b[a == "bmw",1:])

c = a == "bmw"
#print(b[~c])

d = (a == "bmw") | (a == "audi")
#print(d)
#print(b[d])

#b[b < 50] = 50

b[a == "bmw"] = 0
print(b)