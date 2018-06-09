import numpy as np
import matplotlib.pylab as plt
from gradient_1d import function_1
from gradient_1d import numerical_diff

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)

numerical_diff(function_1, 10)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()
