from numpy import *

def f(bin_no):
	idn,mag=loadtxt('Mag_avg.txt', unpack='true')
	mi=min(mag)
	ma=max(mag)
	bins=linspace(mi,ma,bin_no+1)
	count=zeros(int(bin_no), float)
	c=1
	for k in range(bin_no):
		bin_id=[]
		bin_mag=[]
		for (i,j) in zip(idn, mag):
			if (j>=bins[k] and j<bins[k+1]):
				bin_id.append(i)
				bin_mag.append(j)
				count[k]+=1
		data =column_stack((bin_id, bin_mag))
		savetxt('Bins{0}.txt'.format(c), data, fmt = '%s')
		c+=1					
	print(count)

f(5) #input the number of bins
