import numpy as np
import math
import matplotlib.pyplot as plt
import random

#print("Monte Carlo integration method to compute the area of 2D donut")

#print("============INFORMATION============")
r_outer = 1
r_inner = 0.5
actual_area = (math.pi * r_outer * r_outer) - (math.pi * r_inner * r_inner)

'''
print("Outer Circle Radius: " , r_outer)
print("Inner Circle Radius: " , r_inner)
print("Number of points: " , n_points)
'''



ni = []
err = []
areas_calculated = []

for n in range(1,5000,2):
    n_points = n
    x = []
    y = []
    for j in range(n_points):
        x.append(random.uniform(-1*r_outer, r_outer))
        y.append(random.uniform(-1*r_outer, r_outer))
    
    points_enclosed = 0
    for i in range(len(x)):
        if (x[i] <= -0.5 and x[i] >= -1.0) or (x[i] >= 0.5 and x[i] <= 1.0):
            if (y[i] <= -0.5 and y[i] >= -1.0) or (y[i] >= 0.5 and y[i] <= 1.0):
                points_enclosed += 1
                
    calculated_area = ((r_outer*2)**2) * (points_enclosed / n_points)
    error_num = abs(calculated_area - actual_area) / actual_area
    areas_calculated.append(calculated_area)
    ni.append(n_points)
    err.append(error_num)

    
print("Area of donut: " , actual_area)
print("Average area calculated: ", np.mean(areas_calculated))
print("Average error calculated: ", np.mean(err)) 
plt.plot(ni, err,'b')
plt.title("Number of points vs. Difference in area")
plt.xlabel("Number of points (N)")
plt.ylabel("Error (area difference)")
plt.savefig('result_plot.png')
plt.show()





'''
#Used during testing

print("")
print("==============RESULTS==============")
print("Calculated Area:", calculated_area)
print("          Error:", error_num)

x_outer = np.linspace(-r_outer,r_outer,1000)
y_outer = np.sqrt(-x_outer**2+r_outer**2)
plt.plot(x_outer, y_outer,'b')
plt.plot(x_outer,-y_outer,'b')

x_inner = np.linspace(-r_inner,r_inner,1000)
y_inner = np.sqrt(-x_inner**2+r_inner**2)
plt.plot(x_inner, y_inner,'b')
plt.plot(x_inner,-y_inner,'b')

plt.plot(x, y, "ro")
plt.gca().set_aspect('equal')
plt.show()
'''
