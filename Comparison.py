from numpy import *
def f(n):
	Comparision_star_1_list=['C1 star']
	Comparision_star_2_list=['C2 star']
	Magnitude_diff=['Difference']
	for i in range(1,n+1):
		idn, mag=loadtxt('Bins{0}.txt'.format(i), unpack='true')
		mag_diff=100
		for i in range(len(idn)):
			for j in range (len(idn)):
				if j>i:
					mag_diff_1=abs(mag[i]-mag[j])
					if (mag_diff_1<mag_diff):
						mag_diff=mag_diff_1
						comparision_star=[idn[i], idn[j]]
					#print(i,j)
		Comparision_star_1_list.append(comparision_star[0])
		Comparision_star_2_list.append(comparision_star[1])
		Magnitude_diff.append(mag_diff)
		
	data=column_stack((Comparision_star_1_list, Comparision_star_2_list, Magnitude_diff))
	savetxt('Comparision_stars.txt', data, fmt = '%s')
f(5)
