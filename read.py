from numpy import *
import glob
ID,X_axis_ref,Y_axis_ref=loadtxt('refstars_new.list',usecols=(0,1,2),unpack='True')
Stars=len(ID)
#print(len(Y_axis_ref))
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
	#print('Stars{0}'.format(j))	
data=column_stack((idn,files))
savetxt('Stars_reduced.txt', data, fmt='%s') 
print('done')
