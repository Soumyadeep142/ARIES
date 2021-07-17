import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

ID = 176.0
t, mag, dmag = np.loadtxt('{0}_error.txt'.format(ID), unpack = True, usecols = (0, 1, 2))
t, mag, dmag = zip(*sorted(zip(t, mag, dmag)))
t0 = t[0]

from gatspy.periodic import LombScargleFast
model = LombScargleFast().fit(t, mag, dmag)
periods, power = model.periodogram_auto(nyquist_factor=100)

fig, ax = plt.subplots()
ax.plot(periods, power)
ax.set(xlim=(0.2, 1.4), ylim=(0, 0.8),
       xlabel='period (days)',
       ylabel='Lomb-Scargle Power')

model.optimizer.period_range=(0.2, 1.4)
period = model.best_period
print("period = {0}".format(period))

Phase = []
Phase2 = []
for i in range(len(t)):
    a = (t[i] - t0 / period) - int((t[i] - t0 / period))
    Phase.append(a)

for p in Phase:
    Phase2.append(p + 1)
plt.figure()
plt.scatter(Phase, mag, marker='.')
plt.scatter(Phase2, mag, marker='.', color = '#1f77b4', label = f'ID: {ID}')
plt.legend(loc = 'upper right')
plt.title(f'Period: {period}')
plt.show()