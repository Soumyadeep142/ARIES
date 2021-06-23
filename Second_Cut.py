from numpy import *

idn, mag, error=loadtxt('new_avg_mag_error.txt', usecols=(0,1,3), unpack='true')
print(len(idn))

final_id=[]
final_mag=[]
final_err=[]
c=0
for (i,m,e) in zip(idn,mag,error):
	if (m>13 and m<=14):
		if e<=0.015:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)
	elif (m>14 and m<=15):
		if e<=0.015:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)
	elif (m>15 and m<=16):
		if e<=0.015:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)		
	elif (m>16 and m<=17):
		if e<=0.015:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)
	elif (m>17 and m<=18):
		if e<=0.023:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)
	elif (m>18 and m<=19):
		if e<=0.036:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)
	elif (m>19 and m<=20):
		if e<0.041:
			final_id.append(i)
			final_mag.append(m)
			final_err.append(e)
	c+=1
	print(c)
print(len(final_id))		
data = column_stack((final_id, final_mag, final_err))
savetxt('Second_cut.txt', data, fmt='%s')
