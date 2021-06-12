from numpy import *
import statistics

def f(n):
	filename=[]
	SD_list=[]
	for i in range(1, n+1):
		mag=loadtxt('Bins{0}.txt'.format(i), usecols=(1), unpack='true')
		SD=statistics.stdev(mag)
		filename.append('Bins{0}'.format(i))
		SD_list.append(SD)
	data=column_stack((filename, SD_list))
	savetxt('SD_list.txt', data, fmt = '%s')

f(5)
