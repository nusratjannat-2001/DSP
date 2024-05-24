import numpy as np
import matplotlib.pyplot as plt

# Define the sequences
x = np.array([1, 2, 3, 4, 5])
h = np.array([2, 3, 4])

# Reverse the sequence h for correlation
h_reversed = h[::-1]

# Calculate the correlation
def correlation(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1
    y = np.zeros(len_y)

    # Compute the correlation
    for n in range(len_y):
        sum = 0
        for k in range(len_h):
            if 0 <= n - k < len_x:
                sum += x[n - k] * h[k]
        y[n] = sum

    return y

y = correlation(x, h_reversed)

# Generate the x-axis values
n = np.arange(len(y))

# Plot the correlation
plt.stem(n, y)
plt.xlabel('n')
plt.ylabel('Correlation y(n)')
plt.title('Correlation of x(n) and h(n)')
plt.grid(True)
plt.show()

# Print the correlation values
print("Correlation y(n):", y)
