import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-7.5,7.5,500)
f = np.cos(x**2)

plt.plot(x,f)
plt.ylim(-1.5,1.5)
plt.title('f(x) = cos(x^2)')
plt.show()