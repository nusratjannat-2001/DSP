import numpy as np
import matplotlib.pyplot as plt

N = 10
n = np.arange(N)
print(n)
x = np.ones(N)
print(x)
plt.subplot(2, 2, 1)
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Unit Step Sequence')
plt.savefig('unit_step_sequence.png')  # Save plot to a file