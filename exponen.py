import numpy as np
import matplotlib.pyplot as plt

N = 15
n = np.arange(N)
x2 = 0.8 ** n

plt.subplot(2, 2, 3)
plt.stem(n, x2)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Exponential Sequence')

plt.savefig('Exponential_Sequence.png')  # Save plot to a file