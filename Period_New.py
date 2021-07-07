
from numpy import *
import pandas as pd
import statistics
data2=[]
data3=[]
data4=[]
for no in range(3,8): #Bin number
	def clean_list(A):
		return [x for x in A if str(x) != 'nan']
		
	frame, JD=loadtxt("JD_N_R.list", dtype='str', unpack=True)

	df=pd.read_csv('second_cut_stars_with_files.csv')
	df.reset_index(drop=True, inplace=True)
	df.set_index('ID', inplace=True)

	df_mag=pd.read_csv('matching_mags.csv')
	df_mag.reset_index(drop=True, inplace=True)
	df_mag.set_index('ID', inplace=True)

	Var_idn=loadtxt('Variable{0}.txt'.format(no))
	Com_idn=loadtxt("Comparison{0}.txt".format(no))

	Star1=Com_idn[0]
	C1=(df.loc[Star1].tolist())
	C1=clean_list(C1)
	
	Star2=Com_idn[1]
	C2=df.loc[Star2].tolist()
	C2=clean_list(C2)
	
	for i in range(len(Var_idn)):
		print(i+1, len(Var_idn), 'Bin no {0}'.format(no))
		T=(df.loc[Var_idn[i]].tolist())
		T=clean_list(T)
		
		S1=int(Var_idn[i])
		S2=int(Star1)
		common1=intersect1d(T,C1)
		Time=[]
		mag_diff_array=[]
		for std_i in common1:
			#Finding the time
			ps=where(frame==std_i)
			time=JD[ps].item()
			Time.append( round(float(time),6))
			mag1=float(df_mag.loc[S1][std_i])
			mag2=float(df_mag.loc[S2][std_i])
			mag_diff=mag1-mag2
			mag_diff_array.append(mag_diff)
		
		S2=int(Star2)	
		common2=intersect1d(T,C2)
		
		for std_i in common2:
			if std_i not in common1:
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
			if (i>=avg-2*SD and i<=avg+2*SD):
				mag_diff_new.append(i)
				Time_new.append(j)


		updated_time = []
		updated_mag_diff = []
		Time_New,mag_diff_new=zip(*sorted(zip(Time_new, mag_diff_new)))
		'''
		for t1, m1 in zip(Time_new, mag_diff_new):
			for t2, m2 in zip(Time_new, mag_diff_new):
				if t2 > t1:
					if (t2 - t1 < 0.003472 and m2 - m1 > 0.3) or (t2 - t1 < 1 and m2 - m1 > 0.4) or (m2 - m1 > 0.5):
						updated_time.append(t1)
						updated_mag_diff.append(m1)
		'''
		
		y=0
		while y<len(Time_New)-1:
			t1=Time_new[y]
			t2=Time_new[y+1]
			m1=mag_diff_new[y]
			m2=mag_diff_new[y+1]
			if (t2 - t1 < 0.003472 and abs(m2 - m1) > 0.3) or (t2 - t1 < 1 and abs(m2 - m1) > 0.4) or (abs(m2 - m1) > 0.5):
				pass
			else:
				updated_time.append(t1)
				updated_mag_diff.append(m1)
			y=y+1				
				
		data=column_stack((updated_time, updated_mag_diff))
		savetxt('{0}.txt'.format(S1), data, fmt='%s')
		if len(updated_mag_diff) <= 0.25*746:
			data3.append(S1)
		else:
			data4.append(S1)
		data2.append(S1)
savetxt('Period.txt', sort(data2), fmt='%s')
savetxt('Non_Thresold.txt', sort(data3), fmt='%s')
savetxt("Thresold.txt", sort(data4), fmt='%s')
