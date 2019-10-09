import numpy as np
#import matplotlib.pyplot as plt

x = [0,0.25,0.5,0.75,1]
# x regional boundaries.

tp = 1/(3**(1/2))
tm = -tp
# t conversions.

Fm1 = (1/8)*(np.cos(((x[1]-x[0])/2*tm + (x[1]+x[0])/2)**2))
Fp1 = (1/8)*(np.cos(((x[1]-x[0])/2*tp + (x[1]+x[0])/2)**2))
Fm2 = (1/8)*(np.cos(((x[2]-x[1])/2*tm + (x[2]+x[1])/2)**2))
Fp2 = (1/8)*(np.cos(((x[2]-x[1])/2*tp + (x[2]+x[1])/2)**2))
Fm3 = (1/8)*(np.cos(((x[3]-x[2])/2*tm + (x[3]+x[2])/2)**2))
Fp3 = (1/8)*(np.cos(((x[3]-x[2])/2*tp + (x[3]+x[2])/2)**2))
Fm4 = (1/8)*(np.cos(((x[4]-x[3])/2*tm + (x[4]+x[3])/2)**2))
Fp4 = (1/8)*(np.cos(((x[4]-x[3])/2*tp + (x[4]+x[3])/2)**2))
# regional approximations for F(x) = integral of cos(x^2) dx from 0 to 1.
# each region has a width of 1/4.

F = Fm1 + Fp1 + Fm2 + Fp2 + Fm3 + Fp3 + Fm4 + Fp4
# sum of regional approximations; total approximation.

xEXACT = np.linspace(0,1,100)
yEXACT = np.cos(xEXACT**2)
# more accuracte representation of x and cos(x^2)
FEXACT = 0.9045242379002721

print('The 1st interpolation integrates to',Fm1+Fp1,'.')
print('The 2nd integrates to',Fm2+Fp2,'.')
print('The 3rd integrates to',Fm3+Fp3,'.')
print('The 4th integrates to',Fm4+Fp4,'.')
print('The total approximation is',F,'.')
print('The error is',abs(FEXACT-F),'.')