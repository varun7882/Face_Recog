from matplotlib import pyplot as plt
import numpy as np
x=np.array(range(0,100))
y=x**2
plt.plot(x,y)
x=np.array(range(0,20))
y=x**3
plt.plot(x,y)
plt.show()
