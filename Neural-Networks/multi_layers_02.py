"""

o       o
    o
o       o   o
    o
o       o

- Each node has its own weight that attached with all the next nodes
- bias value will only add at the last node

"""

import math
import numpy as np


x = [0.45,0.19,0.33]
w1 = [[0.21,0.15,0.4],
      [0.06,0.24,0.35]]

hidden_value_1 = np.dot(x,np.array(w1).T)
# print(hidden_value_1)

w2 = [[0.23,0.19],
      [0.399,0.42],
      [0.27,0.22]]

hidden_value_2 = np.dot(hidden_value_1,np.array(w2).T)
# print(hidden_value_2)

w3 = [0.2,0.3,0.1]

output = 0

for i in range(3):
    output += hidden_value_2[i]*w3[i]

# print(output)
b = 0.67

output += b

final_output = 1 / (1 + math.exp(- output))

print(f"Answer = {final_output}")