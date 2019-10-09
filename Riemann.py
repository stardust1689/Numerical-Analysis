import numpy as np

x = np.arange(0,1,0.01)
# Widths for area calculation.

y = np.cos(x**2)
# Heights for area calculation.

Al = 0.01*y
# List of individual areas for each slice.

A = 0
# Total area initialized at zero for for loop.

for n in Al:
    A = A+n
    
FEXACT = 0.9045242379002721
# Closest approximation from internet.

print('Total approximation:',A)
print('Error:',abs(A-FEXACT))