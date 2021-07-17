import numpy as np
import matplotlib.pyplot as plt

ID, P_1, P_2, P_3 = np.loadtxt('Updated_Period.txt', unpack = True, usecols = (0, 1, 2, 3))

for i, p in zip(ID, P_2):
    if np.isnan(p) == False:

        Phase = []
        Phase_2 = []
        t, m, e = np.loadtxt(f'{i}_error.txt', usecols=(0, 1, 2), unpack=True)
        t, m, e = zip(*sorted(zip(t, m, e)))
        t0 = t[0]

        for j in range(len(t)):
            a = ((t[j] - t0) / p) - int(((t[j] - t0) / p))
            Phase.append(a)

        for k in Phase:
            Phase_2.append(k + 1)

        Range = max(m) - min(m)
        plt.figure(figsize=(12, 6))
        plt.ylim(min(m) - 0.3 * Range, max(m) + 0.3 * Range)
        plt.scatter(Phase, m, marker='.')
        plt.scatter(Phase_2, m, marker='.', color='#1f77b4', label=f'ID: {i}')
        plt.legend(loc='upper right')
        plt.xlabel('Phase')
        plt.ylabel('T - C (mag)')
        plt.title(f'Period: {p} days')
        plt.savefig(f"D:\\SRFP Reference Materials\\bhumika_taneja\\data_NMS_I\\Potential Variables\\Plots 2\\{i}_plot2.png")

