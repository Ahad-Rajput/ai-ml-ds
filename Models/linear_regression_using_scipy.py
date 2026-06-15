from scipy import stats
import matplotlib.pyplot as plt
import random

x_data = [5,6,2,10,15,20,7,8]
y_data = [50,55,25,110,150,180,80,90]

# x_data = [random.randint(10,50) for _ in range(20)]
# y_data = [random.randint(10,200) for _ in range(20)]

m, c, r, p, err = stats.linregress(x_data, y_data)

""" 
    m:          slop. it shows the change in x & y relation.
    c:          intercept.
    r:          correlation coefficient.
    p:          measures whether the relationship is statistically significant. if less than 0.05. it means relation is significant. above 0.05, then due to randomness.
    err:        standard error. 
"""

lin_mdl = [m * x + c for x in x_data]

plt.scatter(x_data, y_data)
plt.plot(x_data, lin_mdl)
plt.show()

print(r)