import numpy as np
import pandas as pd
import math
import statistics

no =
#for no in range(2,8):
#For clearing the nan elements
def clean_list(A):
	return [x for x in A if str(x) != 'nan']
		

df = pd.read_csv('stars_with_files.csv')
df.reset_index(drop=True, inplace=True)
df.set_index('ID', inplace=True)

Tar_id = np.loadtxt("Target_{0}.txt".format(no))
Com_id = np.loadtxt('Comparison_{0}.txt'.format(no))
print('Total number of target stars: ', len(Tar_id))

df_mag = pd.read_csv('matching_magnitudes.csv')
df_mag.reset_index(drop=True, inplace=True)
df_mag.set_index('ID', inplace=True)

C1 = Com_id[0]
C2 = Com_id[1]

A = (df.loc[C1].tolist())
A = clean_list(A)
B = (df.loc[C2].tolist())
B = clean_list(B)
common = np.intersect1d(A, B)

mag_diff_array = []
for std_i in common:
	mag1 = float(df_mag.loc[C1][std_i])
	mag2 = float(df_mag.loc[C2][std_i])
	mag_diff = mag1 - mag2
	mag_diff_array.append(mag_diff)
SD_Com = statistics.stdev(mag_diff_array)

target_dict = dict()
for i in Tar_id:
	target_dict[i] = []

Potential_Variable_Stars = []
#a = 1
for Target in Tar_id:
	#print(a)
	#a += 1
	T = df.loc[Target].tolist()
	T = clean_list(T)
	common = np.intersect1d(A, T)
	mag_diff_array=[]
	for std_i in common:
		mag1 = float(df_mag.loc[Target][std_i])
		mag2 = float(df_mag.loc[C1][std_i])
		mag_diff = mag1 - mag2
		mag_diff_array.append(mag_diff)
	SD_Tar = statistics.stdev(mag_diff_array)
	Mean_Tar = np.mean(mag_diff_array)
	if mag_diff >= Mean_Tar - 3 * SD_Tar and mag_diff <= Mean_Tar + 3 * SD_Tar:
		target_dict[Tar_id].append(mag_diff)
	tc_mag = list()
	tc_mag = target_dict[Tar_id]
	tc_SD = statistics.stdev(tc_mag)
	if tc_SD >= 3 * SD_Com:
		Potential_Variable_Stars.append(Target)




print(f'Potential variables in Bin_{no}:', len(Potential_Variable_Stars))
data = np.column_stack((Potential_Variable_Stars))
np.savetxt('Potential_Variable_{0}.txt'.format(no), data, fmt='%s')
#print(f'Potential variables in Bin_{no}:', len(Potential_Variable_Stars))
