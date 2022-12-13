#krotka - tuple/s

a = (1,2,3,4,5)

print(a)

a = 1,2,3,4,5

print(a)

b = tuple([1,2,3,4])
print(type(b))

c = tuple("tekst")
print(c)

print(c[2])

d = (1,2,3,4),(6,7,8,9)
print(d[0][0])

e = tuple([True, "tekst", [90,10]])
#e[0] = True

print(e)

f = (("a","b"),("c","d"))
#q, w, (e, r) = f

for x, y in f:
    print(f"x={x}, y={y}")


e = 10,10,30,40,50,60
q, w, *rest = e

print(q)
print(w)
print(rest)

print(e.count(10))