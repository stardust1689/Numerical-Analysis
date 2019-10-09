import numpy as np
import matplotlib.pyplot as plt

x0 = np.arange(-5,5.001,0.01)
y0 = 1/(1+x0**2)
# y0 is function in question.

x = np.arange(-5,5.01,10/13)
# For evenly-spaced inputs between 1st and 2nd argument w/ step size
# of (total space)/(number of inputs).
# 2nd argument should be a little higher than max desired input.

y = 1/(1+x**2)
# y is function in question (same as y0).

coef = np.polyfit(x,y,12)
# Generates list of coefficients for polynomial interpolation.

polynomial = np.poly1d(coef)
# Generates polynomial function using coef elements as coefficients
# for each polynomial degree. MAX power goes with 1st element, second max 
# power goes to 2nd element, etc, so the zero power goes with last element.

xp = x0
yp = polynomial(xp)

plt.plot(x0,y0,'r-')
# Plot of the original function.

plt.plot(xp,yp,'b-')
# Plot of the polynomial interpolation.

plt.plot(x,y,'o')
# x and y inputs.

plt.xlabel('x')
plt.ylabel('y')
plt.show()
print(coef)