import numpy as np
import matplotlib.pyplot as plt
ID = np.loadtxt('Final_Period.txt', unpack = True, usecols = (0))
print(ID)
ix=1
for i in ID:
    plt.subplot(5,4,ix)
    i = int(i)
    plt.figure(figsize=(12, 6))
    p, m, e = np.loadtxt(f'{i}_Bin.txt', usecols = (0, 1, 2), unpack = True)
    plt.xlim(0, 2)
    plt.errorbar(p, m, yerr = e, fmt = 'o', color = 'black')
    #plt.show()
    ix+=1
plt.savefig('plot.png')
