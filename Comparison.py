from numpy import *
import pandas as pd
import math
import statistics

no=2 # Bin number

#For clearing the nan elements
def clean_list(A):
	return [x for x in A if str(x) != 'nan']
	
id, x_ref, y_ref =loadtxt('refstars_new.list', usecols = (0, 1, 2), unpack = True)
	
df=pd.read_csv('stars_with_files.csv')
df.reset_index(drop=True, inplace=True)
df.set_index('ID', inplace=True)
idn,mag=loadtxt('Bins{0}.txt'.format(no), usecols=(0,1), unpack='True')

SD_mag_diff=[]
index=[]
for i in range(len(idn)):
	A=(df.loc[idn[i]].tolist())
	A=clean_list(A)
	for j in range(i+1, len(idn)):
		B=(df.loc[idn[j]].tolist())
		B=clean_list(B)

		common=intersect1d(A,B)
		pos1=where(id==idn[i])
		pos2=where(id==idn[j])
		x1 = x_ref[pos1].item()
		y1 = y_ref[pos1].item()
		x2 = x_ref[pos2].item()
		y2 = y_ref[pos2].item()
		print(i,j)
		mag1=[]
		mag2=[]
		a=0
		index.append([idn[i],idn[j]])
		for std in common:
			a+=1
			#print(i,j,a,len(common))
			x_ax,y_ax,magn=loadtxt(std, usecols=(1,2,3), skiprows=3, unpack="True")
			for n in range(len(x_ax)):
				dist = math.dist([x_ax[n], y_ax[n]], [x1, y1])
				if dist <= 2:
					mag1.append(magn[n])
					break
			for n in range(len(x_ax)):
				dist = math.dist([x_ax[n], y_ax[n]], [x2, y2])
				if dist <= 2:
					mag2.append(magn[n])
					break
		#print(len(mag1), len(mag2))
		mag_diff=[]
		for k in range(len(mag1)):
			mag_diff.append(mag1[k]-mag2[k])
		SD_mag_diff.append(statistics.stdev(mag_diff))

SD_mag_diff, index = zip(*sorted(zip(SD_mag_diff, index)))
#print(SD_mag_diff, index)
C1=index[0][0]
C2=index[0][1]
Comparison=[C1, C2]
data =column_stack((Comparison))
savetxt('Comparison{0}.txt'.format(no), data, fmt='%s')
idn=idn.tolist()
idn.remove(C1)
#print(idn)
idn.remove(C2)
data =column_stack((idn))
savetxt('Target{0}.txt'.format(no), data, fmt='%s')
