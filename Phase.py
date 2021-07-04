from numpy import *
from matplotlib.pyplot import *

Var_id=20952
P=0.12247171
Julian_Date, Magnitude=loadtxt('{0}.txt'.format(Var_id), unpack='true')
Julian_Date,Magnitude=zip(*sorted(zip(Julian_Date,Magnitude)))

JD_i=Julian_Date[0]
Phase=[]
for i in range(len(Julian_Date)):
	Phase.append((Julian_Date[i]-JD_i)/P-int((Julian_Date[i]-JD_i)/P))
scatter(Phase, Magnitude,marker='+')
show()
