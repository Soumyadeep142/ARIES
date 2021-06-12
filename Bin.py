from numpy import *

A=loadtxt('Mag_avg.txt', usecols=(1), unpack='true')
print(min(A), max(A))
