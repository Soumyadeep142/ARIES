from numpy import *
import pandas as pd
import math
import statistics


for no in range(2,8):
	#For clearing the nan elements
	def clean_list(A):
		return [x for x in A if str(x) != 'nan']
		
	df=pd.read_csv('stars_with_files.csv')
	df.reset_index(drop=True, inplace=True)
	df.set_index('ID', inplace=True)

	Tar_idn=loadtxt("Target{0}.txt".format(no))
	Com_idn=loadtxt('Comparison{0}.txt'.format(no))
	print(len(Tar_idn))

	df_mag=pd.read_csv('matching_mags.csv')
	df_mag.reset_index(drop=True, inplace=True)
	df_mag.set_index('ID', inplace=True)

	C1=Com_idn[0]
	C2=Com_idn[1]

	A=(df.loc[C1].tolist())
	A=clean_list(A)
	B=(df.loc[C2].tolist())
	B=clean_list(B)
	common=intersect1d(A,B)

	mag_diff_array=[]
	for std_i in common:
		mag1=float(df_mag.loc[C1][std_i])
		mag2=float(df_mag.loc[C2][std_i])
		mag_diff=mag1-mag2
		mag_diff_array.append(mag_diff)
	SD_Com=statistics.stdev(mag_diff_array)

	Potential_Variable_Stars=[]
	a=1
	for Target in Tar_idn:
		print(a)
		a+=1
		T=df.loc[Target].tolist()
		T=clean_list(T)
		common=intersect1d(A,T)
		mag_diff_array=[]
		for std_i in common:
			mag1=float(df_mag.loc[Target][std_i])
			mag2=float(df_mag.loc[C1][std_i])
			mag_diff=mag1-mag2
			mag_diff_array.append(mag_diff)
		SD_Tar=statistics.stdev(mag_diff_array)
		if SD_Tar>=3*SD_Com:
			Potential_Variable_Stars.append(Target)
	data =column_stack((Potential_Variable_Stars))
	savetxt('Variable{0}.txt'.format(no), data, fmt='%s')
