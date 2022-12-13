import pandas as pd
import numpy as np

a = pd.Series([1,2,3,4,5])

print(a)


#print(a.array)
#print(a.index)

###########################################################

b = pd.Series([1,2,-3,-4,5], index=["a","b","c","d","e"])
#print(b)
#print(b.index)

#print(b["c"])
#print(b[["c","d","e"]])

#print(b[b > 0])
#print(b * 2)

#print(np.exp(b))

#print("z" in b)

###########################################################

c = {
    "Key1": "Value1",
    "Key2": "Value2",
    "Key3": "Value3"
}

d = pd.Series(c)
#print(d)
#print(d.to_dict())

e = ["Key1", "Key2", "Key3", "Key40"]
f = pd.Series(c, index=e)
#print(f)

#print(pd.isna(f))
#print(pd.notna(f))

###########################################################