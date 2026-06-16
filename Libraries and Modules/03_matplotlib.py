import matplotlib.pyplot as plt
import random
import pandas as pd

# x_data = [random.randint(10,50) for _ in range(20)]   # get 20 random values between 10-50 for x
# y_data = [random.randint(10,200) for _ in range(20)]  # get 20 random values between 10-200 for y

df = pd.read_csv('data.csv')

x_data = df['rollno']
y_data = df['marks']

# plt.scatter(x_data, y_data)  # to draw scatter plot

# plt.xlabel = 'Area'
# plt.ylabel = 'Price'

# plt.plot(x_data, y_data, color='red')  # to draw line plot (line color: red)

# plt.bar(x_data,y_data)  # to draw bar chart

# plt.pie(x_data,labels=y_data)  # to draw pie chart

# plt.boxplot(x_data)  # to draw box plot

plt.show()

# print("Everything is fine!")