import numpy as np
import matplotlib.pyplot as plot

a = np.arange(20, 30, 0.1)
print(a)

b, c = np.meshgrid(a, a)

print(c)

d = np.sqrt(b ** 2 + c ** 2)

print(d)

plot.imshow(d, cmap=plot.cm.gray, extent=[-5,5,-5,5])
plot.colorbar()
plot.show()