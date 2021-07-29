import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

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
	Final_Phase=list(Final_Phase)
	Final_Magnitude=list(Final_Magnitude)
	Final_Error=list(Final_Error)
	Final_Phase.insert(0, 'Phase')
	Final_Magnitude.insert(0, 'Magnitude')
	Final_Error.insert(0, 'Error')
	t = list(t)
	t.insert(0, 'Time')
	table=[[Final_Phase[k], Final_Magnitude[k], Final_Error[k]] for k in range(len(Final_Phase))]
	table2 = [[t[j], m[j]] for j in range(len(m))
	with open('{0}.txt'.format(i), 'w') as f:
		f.write(tabulate(table))
		  
	with open('{0}.txt'.format(i), 'w') as f:
		f.write(tabulate(table))
