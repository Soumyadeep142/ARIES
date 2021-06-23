from numpy import *
from math import floor, ceil
idn, mag, error=loadtxt('Second_cut.txt', unpack='true')
A=arange(floor(min(mag)), ceil(max(mag))+1, 1)
#Bins=[[]]*(len(A)-1)
#print(Bins)
Final=[]
for i in range(len(A)-1):
	Bins=[]
	for (m,e) in zip(mag,error):
		if (m>A[i] and m<=A[i+1]):
			Bins.append(e)
	Final.append(Bins)
Median=[]
a=0
Median=[]
Range=[]
for i in Final:
	Median.append(median(i))
	Range.append((A[a]+A[a+1])/2)
	a+=1
	
data=column_stack((Range, Median))
savetxt('error_median.txt', data, fmt='%s')
