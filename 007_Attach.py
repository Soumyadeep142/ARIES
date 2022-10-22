from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('cut_Gaia.csv')
plx_list=[float(a) for a in (df['plx'].tolist())]
RA_list=[float(a) for a in (df['RA'].tolist())]
Dec_list=[float(a) for a in (df['Dec'].tolist())]
dist_list=[float(a) for a in (df['dist'].tolist())]
pmRA_list=[float(a) for a in df['pmRA'].tolist()]
pmDE_list=[float(a) for a in df['pmDE'].tolist()]
Gmag_list=[float(a) for a in df['Gmag'].tolist()]
BPmag_list=[float(a) for a in df['BPMag'].tolist()]
RPmag_list=[float(a) for a in df['RPmag'].tolist()]

df1=pd.read_csv('SFO38_GaiaEDR3AndGaiaDistEDR3_10arcmin.csv')
ra_test=[float(a) for a in (df1['ra'].tolist())]
dec_test=[float(a) for a in (df1['dec'].tolist())]
plx=[float(a) for a in (df1['parallax'].tolist())]
plx_error=[float(a) for a in (df1['parallax_error'].tolist())]
ra_error=[float(a) for a in (df1['ra_error'].tolist())]
dec_error=[float(a) for a in (df1['dec_error'].tolist())]
pmra_error=[float(a) for a in (df1['pmra_error'].tolist())]
pmde_error=[float(a) for a in (df1['pmdec_error'].tolist())]

plx_new=[]
plx_error_new=[]
ra_error_new=[]
dec_error_new=[]
pmra_error_new=[]
pmde_error_new=[]
RA_new=[]
Dec_new=[]
plx_list_new=[]
dist_list_new=[]
pmRA_list_new=[]
pmDE_list_new=[]
Gmag_list_new=[]
BPmag_list_new=[]
RPmag_list_new=[]
for (k,l,m,n,o,p,q,r) in zip(ra_test, dec_test, plx, plx_error, ra_error, dec_error, pmra_error, pmde_error):
	for (i,j,s,t,u,v,w,x,y) in zip(RA_list, Dec_list, plx_list, dist_list, pmRA_list, pmDE_list, Gmag_list, BPmag_list, RPmag_list):
	#for (k,l,m,n,o,p,q,r) in zip(ra_test, dec_test, plx, plx_error, ra_error, dec_error, pmra_error, pmde_error):
		if i==k:
			if j==l:
				RA_new.append(float(i))
				Dec_new.append(float(j))
				plx_list_new.append(float(s))
				dist_list_new.append(float(t))
				pmRA_list_new.append(float(u))
				pmDE_list_new.append(float(v))
				Gmag_list_new.append(float(w))
				BPmag_list_new.append(float(x))
				RPmag_list_new.append(float(y))
				plx_new.append(float(m))
				plx_error_new.append(float(n))
				ra_error_new.append(float(o))
				dec_error_new.append(float(p))
				pmra_error_new.append(float(q))
				pmde_error_new.append(float(r))

dict = {'RA': RA_new, 'Dec': Dec_new, 'plx': plx_list_new, 'dist': dist_list_new, 'pmRA': pmRA_list_new, 'pmDE': pmDE_list_new, 'Gmag': Gmag_list_new, 'BPMag': BPmag_list_new, 'RPmag': RPmag_list_new, 'parallax_new': plx_new, 'plx_error': plx_error_new, 'ra_error': ra_error_new, 'dec_error': dec_error_new, 'pmRA_error': pmra_error_new, 'pmDE_error': pmde_error_new}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('Attach_cut_Gaia.csv')

