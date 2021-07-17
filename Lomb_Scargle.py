import numpy as np
from gatspy.periodic import LombScargleFast

ID = np.loadtxt('Period.txt', unpack = True, usecols = (0))
#print(len(ID))
P_1 = []
P_2 = []
P_3 = []
P_4 = []
for i in ID:
    print('ID: ', i)
    t, m, e = np.loadtxt(f'{i}_error.txt', usecols = (0, 1, 2), unpack = True)
    model = LombScargleFast().fit(t, m, e)
    periods, power = model.periodogram_auto(nyquist_factor=100)
    try:
        model.optimizer.period_range = (0.007, 3.0)
        period = model.find_best_periods(n_periods = 2, return_scores = False)

        P_1.append(period[0])
        P_2.append(period[1])
        P_3.append(period[0] / 2)
        P_4.append(period[1] / 2)

    except:

        P_1.append(np.nan)
        P_2.append(np.nan)
        P_3.append(np.nan)
        P_4.append(np.nan)

data = np.column_stack((ID, P_1, P_2, P_3, P_4))
np.savetxt('Updated_Period.txt', data, fmt = '%s')
print('file saved')