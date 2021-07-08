from numpy import *
from matplotlib.pyplot import *

Var_idn, Period=loadtxt('Thresold.txt', usecols=(0,1), unpack='true')

ix=1
j=1
for (Var_id,P) in zip(Var_idn, Period):
	Var_id=int(Var_id)
	Julian_Date, Magnitude=loadtxt('{0}.txt'.format(Var_id), unpack='true')
	Julian_Date,Magnitude=zip(*sorted(zip(Julian_Date,Magnitude)))

	JD_i=Julian_Date[0]
	Phase=[]
	Phase2=[]
	for i in range(len(Julian_Date)):
		Phase.append((Julian_Date[i]-JD_i)/P-int((Julian_Date[i]-JD_i)/P))
	for p in Phase:
		Phase2.append(p+1)
	subplot(2,2,ix)
	#xlabel("Phase")
	#ylabel("Diff Magnitude")
	#grid(color='cyan', ls='--')
	ax =gca()
	ax.axes.yaxis.set_visible(False)
	ax.axes.xaxis.set_visible(False)
	Range=max(Magnitude)-min(Magnitude)
	ylim(min(Magnitude)-0.3*Range,max(Magnitude)+0.3*Range)
	scatter(Phase, Magnitude,marker='.', color='black', label='{0}'.format(Var_id))
	scatter(Phase2, Magnitude, marker='.', color='black')
	legend(loc='best')
	
	if (ix==4):
		savefig("Variable{0}.pdf".format(j))
		ix=0
		j+=1     
		clf()                               
	ix=ix+1
