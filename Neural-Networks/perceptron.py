import math

x = [0.3,0.2,0.1]  # 3 input_values 
w = [0.21,0.25,0.35]  # 3 weight_values
b = 0.6  # bias value

output = 0

for i in range(3):
    output += x[i]*w[i]

output += b

final_output = 1 / (1 + math.exp(-output))  # Performing Sigmoid_function on output

print(f"Answer = {final_output}")


# print("Everything is fine")