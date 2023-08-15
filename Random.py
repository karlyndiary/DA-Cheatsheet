import random

print(random.randrange(10))

print(random.randint(1,10))

# generates a random number in the range [0, 9], with a step of 2 [even numbers] or incase of 7, it'll return 0 or 7
result = random.randrange(0, 10, 7)
print(result)

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()

