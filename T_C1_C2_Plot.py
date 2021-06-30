from numpy import *
import pandas as pd
from matplotlib.pyplot import *
import random



def clean_list(A):
	return [x for x in A if str(x) != 'nan']

frame, JD=loadtxt("JD_N_R.list", dtype='str', unpack=True)
	
df=pd.read_csv('stars_with_files.csv')
df.reset_index(drop=True, inplace=True)
df.set_index('ID', inplace=True)
for no in range(2,8):
	clf()
	idn,mag=loadtxt('Bins{0}.txt'.format(no), usecols=(0,1), unpack='True')
	Tar_idn=loadtxt("Target{0}.txt".format(no))
	Com_idn=loadtxt('Comparison{0}.txt'.format(no))

	df_mag=pd.read_csv('matching_mags.csv')
	df_mag.reset_index(drop=True, inplace=True)
	df_mag.set_index('ID', inplace=True)
	SD_mag_diff=[]
	index=[]
	mag_diff_all=[]
	index_all=[]
	Time_Frame=[]

	n=random.randint(0,len(Tar_idn)-1)
	C1=Com_idn[0]
	C2=Com_idn[1]
	T=Tar_idn[n]
	
	#C1-C2
	A=(df.loc[C1].tolist())
	A=clean_list(A)
	B=(df.loc[C2].tolist())
	B=clean_list(B)
	common=intersect1d(A,B)

	mag_diff_array=[]
	Time=[]
	ax3=subplot(3,1,3)	
	for std_i in common:
		#Finding the time
		ps=where(frame==std_i)
		time=JD[ps].item()

		Time.append( round(float(time)-2450000,6))
		mag1=float(df_mag.loc[C1][std_i])
		mag2=float(df_mag.loc[C2][std_i])
		mag_diff=mag1-mag2
		mag_diff_array.append(mag_diff)
	scatter(Time,mag_diff_array, s=3, color='red')
	grid(color='black', ls='--')
	xlim(0,5700)
	title('C1 - C2', size=6)
	ylabel('Diff Mag')
	ylim(-1.5,1.5)
	xlabel("JD Date")

	setp(ax3.get_xticklabels(),fontsize=6)
	#T-C1
	A=(df.loc[T].tolist())
	A=clean_list(A)
	B=(df.loc[C1].tolist())
	B=clean_list(B)
	common=intersect1d(A,B)

	mag_diff_array=[]
	Time=[]
	figsize=(15,10)
	suptitle('Magnitude Range-{0}-{1}'.format(round(min(mag)), round(max(mag))))
	ax1=subplot(3,1,1, sharex=ax3)	
	for std_i in common:
		#Finding the time
		ps=where(frame==std_i)
		time=JD[ps].item()

		Time.append( round(float(time)-2450000,6))
		mag1=float(df_mag.loc[T][std_i])
		mag2=float(df_mag.loc[C1][std_i])
		mag_diff=mag1-mag2
		mag_diff_array.append(mag_diff)
	scatter(Time,mag_diff_array, s=3, color='red')
	grid(color='black', ls='--')
	xlim(0,5700)
	ylim(-1.5,1.5)
	title('T - C1', size=6)
	ylabel('Diff Mag')
	setp(ax1.get_xticklabels(), visible=False)
	#T-C2
	A=(df.loc[T].tolist())
	A=clean_list(A)
	B=(df.loc[C2].tolist())
	B=clean_list(B)
	common=intersect1d(A,B)

	mag_diff_array=[]
	Time=[]
	ax2=subplot(3,1,2, sharex=ax3)	
	for std_i in common:
		#Finding the time
		ps=where(frame==std_i)
		time=JD[ps].item()

		Time.append( round(float(time)-2450000,6))
		mag1=float(df_mag.loc[T][std_i])
		mag2=float(df_mag.loc[C2][std_i])
		mag_diff=mag1-mag2
		mag_diff_array.append(mag_diff)
	scatter(Time,mag_diff_array, s=3, color='red')
	grid(color='black', ls='--')
	xlim(0,5700)
	title('T - C2',size=6)
	ylabel('Diff Mag')
	ylim(-1.5,1.5)
	setp(ax2.get_xticklabels(), visible=False)
	savefig('Bin{0}.png'.format(no))
	
	print(no)
