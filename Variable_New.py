import numpy as np
import pandas as pd
import math
import statistics

#Bin number
no = 7
#for no in range(2,8):
#For clearing the nan elements
def clean_list(A):
	return [x for x in A if str(x) != 'nan']


df=pd.read_csv('second_cut_stars_with_files.csv')
df.reset_index(drop=True, inplace=True)
df.set_index('ID', inplace=True)

Tar_idn=np.loadtxt("Target_{0}.txt".format(no))
Com_idn=np.loadtxt('Comparison_{0}.txt'.format(no))
#print(len(Tar_idn))

df_mag=pd.read_csv('matching_magnitudes.csv')
df_mag.reset_index(drop=True, inplace=True)
df_mag.set_index('ID', inplace=True)

C1=Com_idn[0]
C2=Com_idn[1]

A=(df.loc[C1].tolist())
A=clean_list(A)
B=(df.loc[C2].tolist())
B=clean_list(B)
common=np.intersect1d(A,B)

mag_diff_array=[]
for std_i in common:
	mag1=float(df_mag.loc[C1][std_i])
	mag2=float(df_mag.loc[C2][std_i])
	mag_diff=mag1-mag2
	mag_diff_array.append(mag_diff)
Mean_Com=np.mean(mag_diff_array)
SD_Com=statistics.stdev(mag_diff_array)
'''
Final_Mag_diff_array=[]
#Removing Outliers from Comparison Stars
for m in mag_diff_array:
	#print(m)
	if m >= Mean_Com - 3 * SD_Com and m <= Mean_Com + 3 * SD_Com:
		Final_Mag_diff_array.append(m)
SD_Com=statistics.stdev(Final_Mag_diff_array)
'''

Potential_Variable_Stars=[]
a=1
for Target in Tar_idn:
	print(a)
	a+=1
	T=df.loc[Target].tolist()
	T=clean_list(T)
	common1=np.intersect1d(A,T)
	mag_diff_array=[]
	for std_i in common1:
		mag1=float(df_mag.loc[Target][std_i])
		mag2=float(df_mag.loc[C1][std_i])
		mag_diff=mag1-mag2
		mag_diff_array.append(mag_diff)

	common2=np.intersect1d(B,T)
	for std_i in common2:
		if std_i not in common1:
			mag1=float(df_mag.loc[int(Target)][std_i])
			mag2=float(df_mag.loc[int(C2)][std_i])
			mag_diff=mag1-mag2
			mag_diff_array.append(mag_diff)
		
	Mean_Tar=np.mean(mag_diff_array)
	SD_Tar=statistics.stdev(mag_diff_array)
	Final_mag_diff_array=[]
	#Removing Outliers from Target
	for m in mag_diff_array:
		if m >= Mean_Tar - 2 * SD_Tar and m <= Mean_Tar + 2 * SD_Tar:
			Final_mag_diff_array.append(m)
				
	SD_Tar=statistics.stdev(Final_mag_diff_array)
	if SD_Tar >= 3 * SD_Com:
		Potential_Variable_Stars.append(Target)
if len(Potential_Variable_Stars)==0:
	Potential_Variable_Stars.append('Nan')
data = np.column_stack((Potential_Variable_Stars))
print(f'No of potential variables: {len(Potential_Variable_Stars)}')
np.savetxt('Potential_Variables_{0}.txt'.format(no), data, fmt='%s')
