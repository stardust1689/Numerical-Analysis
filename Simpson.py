import numpy as np
import matplotlib.pyplot as plt

x = [0,0.25,0.5,0.75,1]
# x regional boundaries.
y = []
# empty list for y, to be filled by for loop.

h = 0.25
# space within regions.

for n in x:
    y.append(np.cos(n**2))
    
F1 = h/6*(y[0] + 4*(np.cos(((x[0]+x[1])/2)**2)) + y[1])
F2 = h/6*(y[1] + 4*(np.cos(((x[1]+x[2])/2)**2)) + y[2])
F3 = h/6*(y[2] + 4*(np.cos(((x[2]+x[3])/2)**2)) + y[3])
F4 = h/6*(y[3] + 4*(np.cos(((x[3]+x[4])/2)**2)) + y[4])
# regional approximations for F(x) = integral of cos(x^2) dx from 0 to 1.
# each region has a width of 1/4


F = F1 + F2 + F3 + F4
# sum of regional approximations; total approximation

xEXACT = np.linspace(0,1,100)
yEXACT = np.cos(xEXACT**2)
# more accuracte representation of x and cos(x^2) to be shown for comparison.
FEXACT = 0.9045242379002721

print('The 1st interpolation integrates to',F1,'.')
print('The 2nd integrates to',F2,'.')
print('The 3rd integrates to',F3,'.')
print('The 4th integrates to',F4,'.')
print('The total approximation is',F,'.')
print('The error is',abs(FEXACT-F),'.')

#plt.plot(x,y,'r-')
#plt.plot(xEXACT,yEXACT)
#plt.title('Numerical integration of cos(x^2) dx from 0 to 1 - Trapezoid Rule')
#plt.show()