import matplotlib.pyplot as plt  # lib for graphs
import numpy as np  # lib for math operations

# constants
n = 12  # number of harmonics
w = 2700  # max frequency
N = 64  # number of descrete calls

# function for calculating random signal
def formula(a, w, t, phi):
    return a*np.sin(w*t+phi)


signals = [0]*N  # array of signals
w0 = w/n  # frequency

for harmonic in range(n):

    for t in range(N):
        a = np.random.rand()  # amplitude
        phi = np.random.rand()  # phase
        signals[t] += formula(a, w0, t, phi)

    w0 += w0

print('Mx:', np.average(signals))  # Average
print('Dx:', np.var(signals))  # Dispersion

# plotting 
plt.plot(signals)
plt.xlabel('time')
plt.ylabel('x')
plt.title('Random generated signals')
plt.show()
