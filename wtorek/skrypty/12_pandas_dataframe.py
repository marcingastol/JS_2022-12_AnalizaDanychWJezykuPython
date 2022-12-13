import pandas as pd
import numpy as np

a = {
    "Key1": ["Value1","Value2","Value3","Value4"],
    "Key2": [1,2,3,4],
    "Key3": [24.345,56.6,5.5,46.5]
}

b = pd.DataFrame(a)
print(b)