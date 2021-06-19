from numpy import *
import glob
import pandas as pd
import statistics

def distance(x1,y1,x2,y2):
	return sqrt((x1-x2)**2+(y1-y2)**2)
	
ID,X_axis_ref,Y_axis_ref=loadtxt('refstars_new.list',usecols=(0,1,2),unpack='True')
Stars=len(ID)
stdfiles=[f for f in glob.glob("*.std")]
idn=[]
'''
for i in ID:
	idn.append([i])
print(len(idn))

A=[]
co=1
for std in stdfiles:
	x_std, y_std, mag_std=loadtxt(std, usecols=(1,2,3), skiprows=3, unpack='true')
	s=0
	for i in range(len(x_std)):
		a=0

		for j in ID:
			dist=sqrt((x_std[i]-X_axis_ref[a])**2+(y_std[i]-Y_axis_ref[a])**2)

			if dist<=300:
				idn[a].append(mag_std[i])
				break
			a+=1
		s+=1
		print('std{0} line{1} length{2}'. format(co, s, len(x_std)))
	co+=1


print(idn)
'''
n=5748
A=[ID[n], X_axis_ref[n], Y_axis_ref[n]]
a=0
mag=[]
for std in stdfiles:
	x_std, y_std, mag_std=loadtxt(std, usecols=(1,2,3), skiprows=3, unpack='true')
	for (x,y,z) in zip(x_std, y_std, mag_std):
		dist=distance(x,y,A[1],A[2])
		if dist<=3:
			print(z, std)
			mag.append(z)
			
			break
	a+=1
	print(a)
savetxt('new_op.txt', mag)
