from numpy import *
import pandas as pd
import math
import statistics
from matplotlib.pyplot import *

no=7 # Bin number

#For clearing the nan elements
def clean_list(A):
	return [x for x in A if str(x) != 'nan']
	
#id, x_ref, y_ref =loadtxt('refstars_new.list', usecols = (0, 1, 2), unpack = True)
frame, JD=loadtxt("JD_N_R.list", dtype='str', unpack=True)
	
df=pd.read_csv('second_cut_stars_with_files.csv')
df.reset_index(drop=True, inplace=True)
df.set_index('ID', inplace=True)
idn,mag=loadtxt('Bins{0}.txt'.format(no), usecols=(0,1), unpack='True')

df_mag=pd.read_csv('matching_mags.csv')
df_mag.reset_index(drop=True, inplace=True)
df_mag.set_index('ID', inplace=True)
SD_mag_diff=[]
index=[]
mag_diff_all=[]
index_all=[]
Time_Frame=[]
for i in range(len(idn)):
	A=(df.loc[idn[i]].tolist())
	A=clean_list(A)

	for j in range(i+1, len(idn)):
		B=(df.loc[idn[j]].tolist())
		B=clean_list(B)
		common=intersect1d(A,B)
		index.append([idn[i],idn[j]])
		index_all.append([idn[i],idn[j]])
		print(i,j, len(common))
		mag_diff_array=[]
		Time=[]
		for std_i in common:
			#Finding the time
			ps=where(frame==std_i)
			time=JD[ps].item()

			Time.append( round(float(time)-2450000,6))
			S1=int(idn[i])
			S2=int(idn[j])

			mag1=float(df_mag.loc[S1][std_i])

			mag2=float(df_mag.loc[S2][std_i])
			mag_diff=mag1-mag2
			mag_diff_array.append(mag_diff)
		mag_diff_all.append(mag_diff_array)
		Time_Frame.append(Time)
		SD_mag_diff.append(statistics.stdev(mag_diff_array))
SD_mag_diff, index,mag_diff_all,Time_Frame,index_all =map(list, zip(*sorted(zip(SD_mag_diff, index,mag_diff_all,Time_Frame,index_all))))
#print(SD_mag_diff)
#print(index_all)
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



