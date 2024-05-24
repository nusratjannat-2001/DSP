import numpy as np
import matplotlib.pyplot as plt

# Define x(n) and h(n)
x_n = np.array([1, 2, 3, 4, 5])
h_n = np.array([2, 3, 4])

# Compute length of y(n)
len_y = len(x_n) + len(h_n) - 1

# Initialize y(n) with zeros
y_n = np.zeros(len_y)

# Compute convolution manually
for n in range(len_y):
    for k in range(len(x_n)):
        if n - k >= 0 and n - k < len(h_n):
            y_n[n] += x_n[k] * h_n[n - k]

# Plotting
plt.figure(figsize=(10, 6))

# Plot x(n)
plt.subplot(3, 1, 1)
plt.stem(range(len(x_n)),x_n,'r')
plt.title('x(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot h(n)
plt.subplot(3, 1, 2)
plt.stem(range(len(h_n)), h_n)
plt.title('h(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot y(n)
plt.subplot(3, 1, 3)
plt.stem(range(len_y), y_n)
plt.title('y(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()