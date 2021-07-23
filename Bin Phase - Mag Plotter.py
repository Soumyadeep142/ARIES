import numpy as np
import matplotlib.pyplot as plt
ID = np.loadtxt('Final_Period.txt', unpack = True, usecols = (0))
print(ID)
for i in ID:
    i = int(i)
    plt.figure(figsize=(12, 6))
    p, m, e = np.loadtxt(f'{i}_Bin.txt', usecols = (0, 1, 2), unpack = True)
    plt.xlim(0, 2)
    plt.errorbar(p, m, yerr = e, fmt = 'o', color = 'black')
    #plt.show()
    plt.savefig(f'{i}_plot.png')