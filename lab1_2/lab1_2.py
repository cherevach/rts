import matplotlib.pyplot as plt  # lib for graphs
import numpy as np  # lib for math operations

# constants
n = 12  # number of harmonics
w = 2700  # max frequency
N = 64  # number of descrete calls

# function for calculating random signal
def formula(a, w, t, phi):
    return a*np.sin(w*t+phi)

# function for generation array of signals
def generateSignals(n, w, N):
    signals = [0]*N  # array of signals
    w0 = w/n  # frequency
    for _ in range(n):
        a = np.random.rand()  # amplitude
        phi = np.random.rand()  # phase

        for t in range(N):
            signals[t] += formula(a, w0, t, phi)
        w0 += w0
    return signals

# correlation function
def correlation(signal1, signal2):

    Mx1 = np.average(signal1)  # math expectation
    Mx2 = np.average(signal2)  # math expectation
    sd1 = np.std(signal1)  # standart deviation == sqrt(dispersion)
    sd2 = np.std(signal2)  # standart deviation == sqrt(dispersion)
    length = len(signal1) // 2
    res = []

    for t in range(length):
        covarience = 0

        for l in range(length):
            covarience += (signal1[l]-Mx1)*(signal2[l + t]-Mx2) / (length-1)

        res.append((covarience / sd1 * sd2))

    return res

# autocorrelation function
def autocorrelation(signal):
    return correlation(signal, signal)

signals = generateSignals(n, w, N)
signals_copy = generateSignals(n, w, N)

print('Mx:', np.average(signals))  # Average
print('Dx:', np.var(signals))  # Dispersion

# plotting

# signals 
plt.plot(signals)
plt.plot(signals_copy)
plt.xlabel('time')
plt.ylabel('x')
plt.title('Random generated signals 1, 2')
plt.figure()

# cross-correlation
plt.plot(correlation(signals, signals_copy))
plt.xlabel('time')
plt.ylabel('correlation')
plt.title('cross-correlation')
plt.figure()

# autocorrelation
plt.plot(autocorrelation(signals))
plt.xlabel('time')
plt.ylabel('correlation')
plt.title('autocorrelation')
plt.show()
