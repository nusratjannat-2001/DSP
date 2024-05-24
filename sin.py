import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,0.002,50)
y=5*np.cos(2*np.pi*500*t)
plt.subplot(7,1,1)
plt.plot(t,y,color='red')
plt.xlabel("time")
plt.ylabel('Amplitude')
plt.title('Sinusoidal Sequence')
tn=np.linspace(0,0.002,50)
yn=5*np.cos(2*np.pi*500*tn)
plt.subplot(7,1,3)
plt.stem(tn,yn)
plt.xlabel("time")
plt.ylabel('Discrete Ampli')
yn=5*np.cos(2*np.pi*500*5*tn)
plt.subplot(7,1,5)
plt.stem(5*tn,yn)
plt.xlabel("time")
plt.ylabel(' down sam ')
yn1=5*np.cos(2*np.pi*500*5*(tn+2))
plt.subplot(7,1,7)
plt.stem(5*tn,yn1)
plt.xlabel("time")
plt.ylabel('down sam')


plt.savefig('sinusoidal_Sequence.png')  # Save plot to a file