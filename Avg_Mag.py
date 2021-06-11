from numpy import *
import glob
import pandas as pd

ID,X_axis_ref,Y_axis_ref=loadtxt('refstars_new.list',usecols=(0,1,2),unpack='True')
Stars=len(ID)
stdfiles=[f for f in glob.glob("*.std")]

print(len(stdfiles))
A=[]

for i in range(Stars):
	A.append([ID[i]])

for std in stdfiles:
	id=loadtxt(std, skiprows=3,usecols=(0),unpack='true')
	for j in id:
		if j in ID:
			A[int(j)-1].append(std)
print('stdfiles done')

Star_files=[]
idn=[]
files=[]
for i in range(Stars):
	if (len(A[i])-1)/len(stdfiles)>0.25:
		Star_files.append(A[i])
		
print('Star_files done')
for j in range(len(Star_files)):
	popped=Star_files[j].pop(0)
	idn.append(popped)
	files.append(Star_files[j])
#Reduced file saving
d = {}
for i in range(len(id)):
    d[id[i]] = files[i]
#print(d)


df = pd.DataFrame.from_dict(d, orient = 'index')

#print(df.head)


df.to_csv('stars_reduced.csv')

#Average Magnitude Calculation
mag_sum=[]
for i in idn:
	mag_sum.append(0)
s=0
for std in stdfiles:
	iden,magn=loadtxt(std, skiprows=3, usecols=(0,3), unpack='True')
	j=0
	for i in idn:
		if i in iden:
			pos=where(iden==i)
			mag_sum[j]+=magn[pos].item()
		j+=1
	s+=1
	print(s)
avg_mag=[]
for (j,k) in zip(mag_sum,files):
	avg=j/len(k)
	avg_mag.append(avg)
data =column_stack((idn, avg_mag))
savetxt('Mag_avg.txt', data, fmt = '%s')
