from numpy import *
import statistics

ID, Period=loadtxt("Period.txt", unpack='true')

for i in ID:
	i=int(i)
	Phase, Magnitude, Error=loadtxt('{0}_Phase.txt'.format(i), unpack='true')
	A=arange(floor(min(Phase)), ceil(max(Phase))+0.04, 0.04)
	Plot_Phase=[]
	Plot_Mag=[]
	Plot_Error=[]
	print(i)
	for j in range(len(A)-1):
		Phase_list=[]
		Mag_list=[]
		Err_list=[]
		k=0
		for (p,m,e) in zip(Phase, Magnitude, Error):
			if (p>A[j] and p<=A[j+1]):
				Phase_list.append(p)
				Mag_list.append(m)
				Err_list.append(e)
				k+=1
		

		if k==0:
			pass

		elif k==1:
			
			Plot_Phase.append((A[j]+A[j+1])/2)
			Plot_Mag.append(Mag_list[0])
			Plot_Error.append(0)
			
		else:
			Plot_Phase.append((A[j]+A[j+1])/2)
			Plot_Mag.append(mean(Mag_list))
			SD_error=statistics.stdev(Mag_list)
			std_error=SD_error/sqrt(len(Mag_list))
			Plot_Error.append(std_error)	


	data=column_stack((Plot_Phase, Plot_Mag, Plot_Error))
	savetxt('{0}_Bin.txt'.format(i), data, fmt='%s')
