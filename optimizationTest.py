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
star_names=["Dubhe","Merek","Phecda",
            #"uma",
            "Kochab","Alioth","Mizar","Alkaid"]


X = np.array([
    [1491,1371.5],
    [1512,1076],
    [1946,1031.5],
    #[2035,1262],
    [2104.611084,2530.5],
    [2317,1341.5],
    [2542.772705,1425.772705],
    [2916,1315]
       ])


d  = [ 554.9110289, 555.0900828, 247.0855115, 1270.408577,292.9918941,533.5303355,882.5927713]

X_deg=np.array([[165.9303537,61.75084048],
               [165.4611537,56.38262026],
               [178.4587255,53.69482578],
               [222.6757253,74.15557042],
               [193.5084192,55.95977299],
               [200.9826231,54.92523987] ,
                [206.8841326 ,49.31317793]])



#d_ang=[5.373598527,10.43573227,10.22875873,23.32244175,15.24863056,19.33783731,25.70920705]
#for 1st star
#d_ang=[5.346434388,10.25089654,10.01465973,23.66746581,14.91691936,19.00693821,25.7376449]
#for 4th star
d_ang=[10.01465973,10.01789118,4.45923255,22.92747658,5.28771996,9.628795409,15.92843866]

init_vals = [50, 50]  # for [a, b]
init_vals_ang = [150,50]  # for [ra, de]

best_vals, covar = curve_fit(distances, X, d, p0=init_vals)


real_value=[2035,	1262]

#real_value_ang=[165.9303537,61.75084048]
real_value_ang=[183.8575772	,57.03266376]


print('best_vals: {}'.format(real_value))
print('real_values: {}'.format(best_vals))


best_vals_ang, covar = curve_fit(ang_distances, X_deg, d_ang, p0=init_vals_ang)

print(math.sqrt((real_value_ang[0]-best_vals_ang[0])**2+(real_value_ang[1]-best_vals_ang[1])**2))
print(ang_distances(np.array([[best_vals_ang[0], best_vals_ang[1]]]), real_value_ang[0], real_value_ang[1]))
print('best_vals: {}'.format(best_vals_ang))
print('real_values: {}'.format(real_value_ang))

plt.scatter(X[:, 0], X[:, 1], marker='o')
plt.scatter(best_vals[0], best_vals[1], marker='o')
plt.scatter(real_value[0], real_value[1], marker='*')
for i in range(len(X)):
    plt.annotate("("+ str(round(X_deg[i][0]/15,2))+" "+str(round(X_deg[i][1],2))+")", (X[i][0]+80, X[i][1]-90),fontsize=7)
    plt.annotate(star_names[i], (X[i][0], X[i][1]+30),fontsize=10)
plt.xlim(3500,1200)
plt.ylim(500,3000)
plt.show()


plt.scatter(X_deg[:, 0], X_deg[:, 1], marker='o')
plt.scatter(best_vals_ang[0], best_vals_ang[1], marker='o')
plt.scatter(real_value_ang[0], real_value_ang[1], marker='*')
plt.xlabel("RA")
plt.ylabel("Dec")
#plt.xlim(0,3500)
#plt.ylim(0,3000)
plt.show()