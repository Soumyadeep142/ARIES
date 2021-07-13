from numpy import *
import math
import statistics
import pandas as pd

data2=[]
def clean_list(A):
	return [x for x in A if str(x) != 'nan']

def quadrature(A,B):
	 return sqrt(A**2+B**2)
for no in range(2,8):

	

	frame, JD=loadtxt("JD_N_R.list", dtype='str', unpack=True)
		
	df=pd.read_csv('second_cut_stars_with_files.csv')
	df.reset_index(drop=True, inplace=True)
	df.set_index('ID', inplace=True)

	Tar_idn=loadtxt("Target{0}.txt".format(no))
	Com_idn=loadtxt('Comparison{0}.txt'.format(no))
	#print(len(Tar_idn))

	df_mag=pd.read_csv('matching_mags.csv')
	df_mag.reset_index(drop=True, inplace=True)
	df_mag.set_index('ID', inplace=True)
	
	df_error=pd.read_csv('matching_errors.csv')
	df_error.reset_index(drop=True, inplace=True)
	df_error.set_index('ID', inplace=True)
	
	C1=Com_idn[0]
	C2=Com_idn[1]

	A=(df.loc[C1].tolist())
	A=clean_list(A)
	B=(df.loc[C2].tolist())
	B=clean_list(B)
	
	common=intersect1d(A,B)
	mag_com=[]
	time_com = []
	for std_i in common:
		mag_c1=float(df_mag.loc[C1][std_i])
		mag_c2=float(df_mag.loc[C2][std_i])
		mag_diff=mag_c1-mag_c2
		mag_com.append(mag_diff)
		pos = where(frame == std_i)
		t = JD[pos].item()
		time_com.append(round(float(t), 6))
		
		
	for Target in Tar_idn:
		T=df.loc[Target].tolist()
		T=clean_list(T)
		common1=intersect1d(A,T)
		mag_diff_array=[]
		Time=[]
		err_array=[]
		for std_i in common1:
		#Finding the time
			ps=where(frame==std_i)
			time=JD[ps].item()
			Time.append( round(float(time),6))
			mag1=float(df_mag.loc[Target][std_i])
			mag2=float(df_mag.loc[C1][std_i])
			mag_diff=mag1-mag2
			mag_diff_array.append(mag_diff)
			err1=float(df_error.loc[Target][std_i])
			err2=float(df_error.loc[C1][std_i])
			error=quadrature(err1, err2)
			err_array.append(error)
			
			
			
		common2=intersect1d(B,T)
		for std_i in common2:
			if std_i not in common1:
			#Finding the time
				ps=where(frame==std_i)
				time=JD[ps].item()
				Time.append( round(float(time),6))
				mag1=float(df_mag.loc[int(Target)][std_i])
				mag2=float(df_mag.loc[int(C2)][std_i])
				mag_diff=mag1-mag2
				mag_diff_array.append(mag_diff)
				err1=float(df_error.loc[int(Target)][std_i])
				err2=float(df_error.loc[int(C2)][std_i])
				error=quadrature(err1, err2)
				err_array.append(error)
				
		for x in range(3):
			Mean_Tar=mean(mag_diff_array)
			SD_Tar=statistics.stdev(mag_diff_array)
			Final_mag_diff_array=[]
			Final_time=[]
			Final_err_array=[]
			#Removing Outliers from Target
			for (m,t,e) in zip(mag_diff_array, Time,err_array) :
				if m>=Mean_Tar-2*SD_Tar and m<=Mean_Tar+2*SD_Tar:
					Final_mag_diff_array.append(m)
					Final_time.append(t)
					Final_err_array.append(e)
			mag_diff_array=Final_mag_diff_array
			Time=Final_time
			err_array=Final_err_array
			
		#Removing Sudden Change
		Time, mag_diff_array,err_array=zip(*sorted(zip(Time, mag_diff_array, err_array)))
		j=1
		t1=Time[1]
		t0=Time[0]
		m1=mag_diff_array[1]
		m0=mag_diff_array[0]
		e1=err_array[1]
		e0=err_array[0]
		
		Time_new_list=[]
		Mag_new_list=[]
		Err_new_list=[]
		while j<len(Time)-2:
			if ((t1-t0)<=0.00347):
				if abs(m1-m0)>0.3:
					t0=t0
					m0=m0
					e0=e0
					if t1 in time_com:
						pos = where(time_com == t1)
						delete(time_com, pos)
						delete(mag_com, pos)
				else:
					Time_new_list.append(t0)
					Mag_new_list.append(m0)
					Err_new_list.append(e0)
					t0=t1
					m0=m1
					e0=e1
					
			elif (((t1 - t0) > 0.00347) and (t1 - t0) <= 1):
				if abs(m1-m0)>0.4:
					t0=t0
					m0=m0
					e0=e0
					if t1 in time_com:
						pos = where(time_com == t1)
						delete(time_com, pos)
						delete(mag_com, pos)
				else:
					Time_new_list.append(t0)
					Mag_new_list.append(m0)
					Err_new_list.append(e0)
					t0=t1
					m0=m1
					e0=e1
					
			elif (t1-t0)>1:
				if abs(m1 - m0) > 0.5:
					t0=t0
					m0=m0
					e0=e0
					if t1 in time_com:
							pos = where(time_com == t1)
							delete(time_com, pos)
							delete(mag_com, pos)
			
				else:
					Time_new_list.append(t0)
					Mag_new_list.append(m0)
					Err_new_list.append(e0)
					t0=t1
					m0=m1
					e0=e1
				
			t1=Time[j+1]
			m1=mag_diff_array[j+1]
			j=j+1
		
		SD_com=statistics.stdev(mag_com)
		SD_Tar=statistics.stdev(Mag_new_list)
		if SD_Tar>=3*SD_com:
			data=column_stack((Time_new_list, Mag_new_list))
			savetxt('{0}.txt'.format(Target), data, fmt='%s')
			data2.append(Target)
			data3=column_stack((Time_new_list, Mag_new_list, Err_new_list))
			savetxt('{0}_error.txt'.format(Target), data3, fmt='%s')
savetxt('Period.txt', sort(data2), fmt='%s')
