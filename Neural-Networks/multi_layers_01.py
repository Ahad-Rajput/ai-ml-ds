"""
o
    o
o       o
    o
o

- Each node has its own weight that attached with all the next nodes
- bias value will only add at the last node

"""

import math
import numpy as np

x = [0.3,0.2,-0.1]      # 3 input_values

w1 = [[0.1,0.3,0.35], 
      [0.2,0.2,0.4]]    # 6 weight_values and making a list of list cuz after input layer there are 2 nodes in hidden layer 3 weight_values for each node

hidden_values = np.dot(x,np.array(w1).T)  # Taking transpose of w1 to make martices multiplication possible

"""
shape of x is [1,3]  &  shape of w1 is [2,3]
After Transpose:
shape of x is [1,3]  &  shape of w1 is [3,2]
"""

# print(hidden_values)

w2 = [0.9, 0.3]

b = 0.6   # bias_value

output = np.dot(hidden_values, w2) + b
# print(output)

final_output = 1 / (1 + math.exp(-output))   # Performing Sigmoid_function on output

print(f"Answer = {final_output}")

