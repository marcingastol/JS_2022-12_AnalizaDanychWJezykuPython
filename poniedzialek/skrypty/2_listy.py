a = [1,2,3,"asdasd",2,None]

b = 1,2,3

c = list(b)

print(a)
print(b)
print(type(c))

print(list(range(0,5)))

a.append("asdasd")

a.insert(2, 123)

a.pop(3)

print(a)
a.remove("asdasd")
print(a)

print("asdasd" not in a)

a.extend([1,2,3,4,5])

d = ["asd","f","wefwefewf","bfdb"]
d.sort(key=len)
print(d)

e = [1234,546,36,24,78,25,678,24456,6724,78]
print(e[:-1])