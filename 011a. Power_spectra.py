import numpy as np
from gatspy.periodic import LombScargleFast
from matplotlib.pyplot import *
ID = np.loadtxt('Period.txt', unpack = True, usecols = (0))
#print(len(ID))
P_1 = []
P_2 = []
P_3 = []
P_4 = []
for i in ID:
    print('ID: ', i)
    i=int(i)
    t, m, e = np.loadtxt(f'{i}_error.txt', usecols = (0, 1, 2), unpack = True)
    model = LombScargleFast().fit(t, m, e)
    periods, power = model.periodogram_auto(nyquist_factor=100)

    xlabel('Periods(Days)')
    ylabel('Lomb-Scargle Power')
    xlim(0.2,2)
    
    title("ID: {0}".format(i))
    plot(periods, power, color='black')
    savefig('{0}_power.png'.format(i))
    clf()
