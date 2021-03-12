import matplotlib.pyplot as plt  # lib for graphs
import numpy as np  # lib for math operations
import math  # lib for math operations

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

        for t in range(N):
            a = np.random.rand()  # amplitude
            phi = np.random.rand()  # phase
            signals[t] += formula(a, w0, t, phi)
        w0 += w0
    return signals

# function for calculating Discrete Fourier Transform coefficient
def dftCoeff(pk, N):
    exp = 2*math.pi*pk/N
    return complex(math.cos(exp), -math.sin(exp))

# function for calculating Discrete Fourier Transform 

def dft(signals):
    file = open("lab2_1/Wpk_table.txt", "w") # file with Wpk table values
    N = len(signals)
    spectrum = []
    WpkTable = [[0]*N]*N 
    for p in range(N):
        sum = 0
        for k in range(N):
            WpkTable[p][k] = dftCoeff(p*k, N) # intermediate Wpk values
            sum+= signals[k] * WpkTable[p][k]
        spectrum.append(abs(sum))
    
    for p in range(N):
        for k in range(N):
            file.write("p = {} : k = {} : {} \n".format(str(p),str(k), str(WpkTable[p][k]))) # write Wpk table to file 
    file.close()
       
    return spectrum

signals = generateSignals(n, w, N)

# plotting

# signals
plt.plot(signals)
plt.xlabel('time')
plt.ylabel('x')
plt.title('Random generated signal')
plt.figure()

# dft 
plt.plot(dft(signals))
plt.xlabel('p')
plt.ylabel('F(p)')
plt.title('Descrete Fourier Transform')
plt.show()