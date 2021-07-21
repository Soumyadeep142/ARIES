import numpy as np
import matplotlib.pyplot as plt

ID, Period= np.loadtxt('Period.txt', unpack = True, usecols = (0, 1))

for (i,P) in zip(ID, Period):
	Phase = []
	Phase_2 = []
	i=int(i)
	t, m, e = np.loadtxt(f'{i}_error.txt', usecols=(0, 1, 2), unpack=True)
	t, m, e = zip(*sorted(zip(t, m, e)))
	t0 = t[0]

	for j in range(len(t)):
		a = ((t[j] - t0) / P) - int(((t[j] - t0) / P))
		Phase.append(a)

	for k in Phase:
		Phase_2.append(k + 1)
		
	Final_Phase=Phase+Phase_2
	Final_Magnitude=m+m
	Final_Error=e+e
	Final_Phase, Final_Magnitude, Final_Error = zip(*sorted(zip(Final_Phase, Final_Magnitude, Final_Error )))
	data=np.column_stack((Final_Phase, Final_Magnitude, Final_Error))
	np.savetxt('{0}_Phase.txt'.format(i), data, fmt='%s')

