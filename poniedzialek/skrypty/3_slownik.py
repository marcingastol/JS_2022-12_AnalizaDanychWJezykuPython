a = {
    "key1": "value1",
    "key2": 2,
    "key3": [1,2,3,4]
}

print(a)

a["key4"] = [10,20,30]
a["key2"] = 40
print(a)
print("key2" not in a)

del a["key2"]
print(a)

print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))