"""
o       o
    o
o       o   o
    o
o       o

- Each node in a lyer has bias value except input layer
- Not every node weight attached to next layer nodes
"""

import math
import numpy as np
import random


x = [0.45,0.19,0.33]  # 3 input_values

w1 = [[0.21,1,1],  
      [1,0.24,0.35]]  # 6 weight_values

"""
x1 node = input_value: 0.45 weight_value: 0.21 for 1st_hidden_layer_node and weight_value: 1 means x1 isn't attach with 2nd_hidden_layer_node

x2 node = input_value 0.19 weight_value: 1 means x2 isn't attach with 1st_hidden_layer_node and weight_value: 0.24 for 2nd_hidden_layer_node

"""


hidden_value_1 = np.dot(x,np.array(w1).T)

# print(hidden_value_1)

b1 = [0.6, 0.2]

for i in range(2):
    hidden_value_1[i] += b1[i]

# print(hidden_value_1)

w2 =  [[1,0.19],
      [1,0.42],
      [0.27,0.22]]

hidden_value_2 = np.dot(hidden_value_1, np.array(w2).T)
# print(hidden_value_2)

b2 = [0.27,0.33,0.12]

for i in range(3):
    hidden_value_2[i] += b2[i]

# print(hidden_value_2)

# generating a 1D weight array with random values bw (0-1)  [? ? ?]
w3 = [random.random() for _ in range(3)]   

output = np.dot(hidden_value_2, np.array(w3).T)
print(output)

b3 = 0.10

output += b3

final_output = 1 / (1 + math.exp(- output))  # Performing Sigmoid_function on output
print(final_output)