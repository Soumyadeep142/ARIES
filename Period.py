from numpy import *
import pandas as pd
import statistics

for no in range(2,8): #Bin number
	def clean_list(A):
		return [x for x in A if str(x) != 'nan']
		
	frame, JD=loadtxt("JD_N_R.list", dtype='str', unpack=True)

	df=pd.read_csv('stars_with_files.csv')
	df.reset_index(drop=True, inplace=True)
	df.set_index('ID', inplace=True)

	df_mag=pd.read_csv('matching_mags.csv')
	df_mag.reset_index(drop=True, inplace=True)
	df_mag.set_index('ID', inplace=True)

	Var_idn=loadtxt('Variable{0}.txt'.format(no))
	Com_idn=loadtxt("Comparison{0}.txt".format(no))
	C1=Com_idn[0]
	C=(df.loc[C1].tolist())
	C=clean_list(C)
	for i in range(len(Var_idn)):
		print(i+1, len(Var_idn), 'Bin no {0}'.format(no))
		T=(df.loc[Var_idn[i]].tolist())
		T=clean_list(T)
		
		S1=int(Var_idn[i])
		S2=int(C1)
		common=intersect1d(T,C)
		Time=[]
		mag_diff_array=[]
		for std_i in common:
			#Finding the time
			ps=where(frame==std_i)
			time=JD[ps].item()
			Time.append( round(float(time),6))
			mag1=float(df_mag.loc[S1][std_i])
			mag2=float(df_mag.loc[S2][std_i])
			mag_diff=mag1-mag2
			mag_diff_array.append(mag_diff)
		avg=mean(mag_diff_array)
		SD=statistics.stdev(mag_diff_array)
		mag_diff_new=[]
		Time_new=[]
		for (i,j) in zip(mag_diff_array, Time):
			if (i>avg-3*SD and i<avg+3*SD):
				mag_diff_new.append(i)
				Time_new.append(j)
		data=column_stack((Time_new, mag_diff_new))
		savetxt('{0}.txt'.format(S1), data, fmt='%s')
