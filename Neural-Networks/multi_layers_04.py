""""
o
    o
o       o
    o
o

- Each node in a lyer has bias value except input layer
- Not every node weight attached to next layer nodes
"""

import math
import numpy as np

x = [0.3,0.2,-0.1]      # 3 input_values

w1 = [[0.1,0.3,1], # Here '1' value represents that 1st & 3rd input_node attach with only 1 hidden_node
      [1,0.2,0.4]]    # 6 weight_values and making a list of list cuz after input layer there are 2 nodes in hidden layer 3 weight_values for each node

hidden_values = np.dot(x,np.array(w1).T)  # Taking transpose of w1 to make martices multiplication possible

# print(hidden_values)

b1 = [0.6, 0.2]

for i in range(2):
    hidden_values[i] += b1[i]   # 1st_hidden_layer_node + 1st_bias_value and 2nd_hidden_value + 2nd_bias

print(hidden_values)

w2 = [0.9, 0.3]

output = np.dot(hidden_values, np.array(w2).T)

print(output)

b2 = 0.5

output += b2

final_output = 1/ (1 + math.exp(output))   # Performing Sigmoid_function on output

print(final_output)


