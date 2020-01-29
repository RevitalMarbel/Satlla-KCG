import numpy
from scipy.optimize import *
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import numpy as np

def distances(X, a, b):
    return [np.sqrt((x[0] - a) ** 2 + (x[1] - b) ** 2) for x in X]

def ang_distances(X, ra, dec):
    X_rad = np.radians(X)

    ra = math.radians(ra)
    dec = math.radians(dec)


    a =[ math.sin(y) * math.sin(dec) + math.cos(y) * math.cos(dec) * math.cos(x - ra) for x, y in X_rad]
    #print(a)
    res = np.arccos(a)
    res = np.degrees(res)
    return res

X = np.array([
     [2104.611083984375 ,2530.5] ,
    [1512.0 ,1076.0 ],
    [1946.0 ,1031.5 ] ,
    [2035.0 ,1262.0]
   ])


d  = [1311, 296.2, 568, 554]

X_deg=np.array([
               [165.4611537,56.38262026],
               [178.4587255,53.69482578],
               [183.8575772,57.03266376],
               [222.6757253,74.15557042],
               [193.5084192,55.95977299],
               [200.9826231,54.92523987] ,
                [206.8841326 ,49.31317793]])



#d_ang=[5.373598527,10.43573227,10.22875873,23.32244175,15.24863056,19.33783731,25.70920705]
d_ang=[5.346434388,10.25089654,10.01465973,23.66746581,14.91691936,19.00693821,25.7376449]

init_vals = [1, 1]  # for [a, b]
init_vals_ang = [50,50]  # for [ra, de]

best_vals, covar = curve_fit(distances, X, d, p0=init_vals)


real_value=[1491,1371.5]
real_value_ang=[165.9303537,61.75084048]



print('best_vals: {}'.format(best_vals))
print('real_values: {}'.format(best_vals))


best_vals_ang, covar = curve_fit(ang_distances, X_deg, d_ang, p0=init_vals_ang)

print(math.sqrt((real_value_ang[0]-best_vals_ang[0])**2+(real_value_ang[1]-best_vals_ang[1])**2))

print('best_vals: {}'.format(best_vals_ang))
print('real_values: {}'.format(real_value_ang))

plt.scatter(X[:, 0], X[:, 1], marker='*')
plt.scatter(best_vals[0], best_vals[1], marker='o')
plt.scatter(real_value[0], real_value[1], marker='*')
plt.xlim(0,3500)
plt.ylim(0,3000)
plt.show()


plt.scatter(X_deg[:, 0], X_deg[:, 1], marker='*')
plt.scatter(best_vals_ang[0], best_vals_ang[1], marker='o')
plt.scatter(real_value_ang[0], real_value_ang[1], marker='*')
#plt.xlim(0,3500)
#plt.ylim(0,3000)
plt.show()