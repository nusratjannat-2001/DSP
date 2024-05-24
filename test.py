import numpy as np
import matplotlib.pyplot as plt
# Variables
start = 0
stop = 0.01
phase = 90
frequency = 500
amplitude = 5
sampling_frequency = 9000
samples_count = sampling_frequency * (stop-start)

# Conversion
phase_radian = (phase * np.pi/180)

# Base 
t_base = np.linspace(start=start, stop=stop, num=int(samples_count))
y_base = amplitude * np.sin((2 * np.pi * frequency * t_base) + phase_radian)
# Generate Analog Signal
plt.figure(figsize=(10, 10))
plt.title(f'Continuous Signal')
plt.plot(t_base, y_base)
plt.show()
# Generate Discrete Signal
plt.figure(figsize=(10, 6))
plt.title(f'Discrete Signal')
plt.stem(t_base*9000, y_base)
plt.show()
# Shifting Signal
shift = 2
t_shift = np.linspace(start=-0.004, stop=stop, num=int(samples_count)) + shift*0.0005
y_shift= amplitude * np.sin((2 * np.pi * frequency * t_shift) + phase_radian)
plt.figure(figsize=(10, 6))
plt.title(f'Discrete Signal Shifted by {shift}')
plt.stem(t_shift*9000, y_shift)
plt.show()