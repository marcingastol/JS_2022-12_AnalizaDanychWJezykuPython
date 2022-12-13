import pandas as pd
import numpy as np

a = {
    "Key1": ["Value1","Value2","Value3","Value4","Value5","Value6","Value7","Value8"],
    "Key2": [1,2,3,4,5,6,7,8],
    "Key3": [24.345,56.6,5.5,46.12,5.7,46.9,5.3,46.56]
}

b = pd.DataFrame(a, columns=["Key1","Key3","Key2","Key4"])
#print(b)

#print(b["Key3"])
#print(b.Key3)

#print(b.iloc[3])

#b["Key4"] = np.arange(8)
#print(b)

##############################################################################

c = pd.Series([1,2,3,4], index=["a","b","c","d"])

b["Key5"] = c

#print(b)

del b["Key5"] 
#print(b.columns)

##############################################################################

d = {
    "Key1": {"Value1": 1,"Value2": 1,"Value3": 1,"Value4": 1,"Value5": 1},
    "Key2": {"Value6": 1,"Value7": 1,"Value8": 1,"Value9": 1,"Value10": 1}
}

e = pd.DataFrame(d)

#print(e.T)

f = {
    "Key1": e["Key1"][:-1],
    "Key2": e["Key2"][1:6]
}

g = pd.DataFrame(f)

#print(g)

#print(g.to_numpy())

################################################

b = b.reindex(["a","b","c","d","e","f"])

print(b)