from numpy import *
import pandas as pd

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

	for i in range(len(Var_idn)):
		print(i+1, len(Var_idn), 'Bin no {0}'.format(no))
		T=(df.loc[Var_idn[i]].tolist())
		T=clean_list(T)
		S=int(Var_idn[i])
		Time=[]
		mag_array=[]
		for std_i in T:
			#Finding the time
			ps=where(frame==std_i)
			time=JD[ps].item()
			Time.append( round(float(time),6))
			mag=float(df_mag.loc[S][std_i])
			mag_array.append(mag)
		data=column_stack((Time, mag_array))
		savetxt('{0}.txt'.format(S), data, fmt='%s')
