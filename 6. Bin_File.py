from numpy import *
from math import floor, ceil

idn, mag, error, SD=loadtxt('Third_cut.txt', unpack='true')
A=arange(floor(min(mag)), ceil(max(mag))+1, 1)
#Bins=[[]]*(len(A)-1)
#print(Bins)
for j in range(len(A)-1):
	idx=[]
	magn=[]
	err=[]
	sd=[]
	for (i,m,e,s) in zip(idn,mag,error,SD):
		if (m>A[j] and m<=A[j+1]):
			idx.append(i)
			magn.append(m)
			err.append(e)
			sd.append(s)
	data=column_stack((idx, magn, err, sd))
	savetxt('Bins{0}.txt'.format(j+1), data, fmt='%s')
