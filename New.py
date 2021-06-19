from numpy import *
import glob
import pandas as pd
import statistics

ID,X_axis_ref,Y_axis_ref=loadtxt('refstars_new.list',usecols=(0,1,2),unpack='True')
Stars=len(ID)
stdfiles=[f for f in glob.glob("*.std")]
idn=[]

for i in ID:
	idn.append([i])
print(len(idn))

A=[]
co=1
for std in stdfiles:
	x_std, y_std, mag_std=loadtxt(std, usecols=(1,2,3), skiprows=3, unpack='true')
	s=0
	for (x,y,z) in zip(x_std, y_std, mag_std):
		a=0

		for i in ID:
			dist=sqrt((x-X_axis_ref[a])**2+(y-Y_axis_ref[a])**2)

			if dist<=300:
				idn[a].append(z)
				break
			a+=1
		s+=1
		print('std{0} line{1} length{2}'. format(co, s, len(x_std)))
	co+=1


print(idn)
