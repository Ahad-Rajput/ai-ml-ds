from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import random


# x_data = [5,6,2,10,15,20,7,8]
# y_data = [50,55,25,110,150,180,80,90]


x_data = [random.randint(10,50) for _ in range(20)]
y_data = [random.randint(10,200) for _ in range(20)]


x_data = np.array(x_data)[:, np.newaxis]    # Convert 1D to 2D 


lin_mdl = linear_model.LinearRegression()   # Creating model
lin_mdl.fit(x_data, y_data)

print(lin_mdl.predict([[50]]))


plt.scatter(x_data, y_data)  # draw scatter plot

plt.plot(x_data, lin_mdl.predict(x_data), color='orange')  # plot regression line

plt.show()

# print("Everything is fine!")