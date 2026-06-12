"""

o
    o       o
o       o       o
    o       o       o
o       o       o
    o       o
o

- Each node has its own weight that attached with all the next nodes
- bias value will only add at the last node

"""

import math
import numpy as np

x = [0.5, 1, 0.8, 0.3]

w1 = [[0.81, 0.12, 0.92, 0.27],
      [0.33, 0.44, 0.72, 0.15],
      [0.29, 0.37, 0.27, 0.53]]


hidden_values_1 = np.dot(x, np.array(w1).T)
# print(hidden_values_1)

w2 = [[0.3, 0.9, 0.2],
      [0.1, 0.3, 0.5]]

hidden_values_2 = np.dot(hidden_values_1, np.array(w2).T)
# print(hidden_values_2)

w3 = [[-1.5, 0.1],
      [1,-3],
      [0.22, 0.77]]

hidden_values_3 = np.dot(hidden_values_2, np.array(w3).T)
# print(hidden_values_3)

w4 = [[0.73, -1.8, 0.2],
      [-0.2, 0.6, 1.2]]

hidden_values_4 = np.dot(hidden_values_3,np.array(w4).T)
# print(hidden_values_4)

w5 = [0.2,0.4]

output = np.dot(hidden_values_4, np.array(w5).T)
# print(output)


b = 1.6

output += b

final_output = 1 / (1 + math.exp(- output))
print(final_output)