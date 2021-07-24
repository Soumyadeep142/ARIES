import numpy as np
import pandas as pd
from tabulate import tabulate

ID = np.loadtxt('refstars_new.list', unpack = True, usecols = (0))
X, Y, RA, DEC = np.loadtxt('refstars_new.list', unpack = True, usecols = (1, 2, 3, 4), dtype = str)
final_id, period = np.loadtxt('Final_Period.txt', unpack = True, usecols = (0, 1))


def clean_list(A):
    return [x for x in A if str(x) != 'nan']

df_mag = pd.read_csv('matching_magnitudes.csv')
df_mag.reset_index(drop=True, inplace=True)
df_mag.set_index('ID', inplace=True)

ra_list = []
dec_list = []
period_list = []
x_list = []
y_list = []
mag_list = []

for j in range(len(ID)):
    ID[j] = int(ID[j])
    #print(type(ID[j]))
    for i in range(len(final_id)):
        final_id[i] = int(final_id[i])
        #print(type(i))
        if final_id[i] == ID[j]:
            r = RA[j]
            d = DEC[j]
            x = X[j]
            y = Y[j]
            p = period[i]
            ra_list.append(r)
            dec_list.append(d)
            x_list.append(x)
            y_list.append(y)
            period_list.append(round(p, 5))

for i in final_id:
    S = df_mag.loc[i].tolist()
    S = clean_list(S)
    mags = []
    for e in S:
        if e != -1.0:
            mags.append(e)
    m = np.mean(mags)
    mag_list.append(round(m, 3))

#print(len(mag_list))
        

final_id, x_list, y_list, ra_list, dec_list, mag_list, period_list = zip(*sorted(zip(final_id, x_list, y_list, ra_list, dec_list, mag_list, period_list)))
#print(len(ra_list), len(dec_list), len(period_list))
final_id=list(final_id)
x_list=list(x_list)
y_list=list(y_list)
ra_list=list(ra_list)
dec_list=list(dec_list)
mag_list=list(mag_list)
period_list=list(period_list)
final_id.insert(0, "ID")
x_list.insert(0, 'X-axis')
y_list.insert(0, 'Y-axis')
ra_list.insert(0, 'RA(J2000)')
dec_list.insert(0, 'Dec(J2000)')
mag_list.insert(0, 'R(mag)')
period_list.insert(0, 'Period(days)')
table=[[final_id[k], x_list[k], y_list[k], ra_list[k], dec_list[k], mag_list[k], period_list[k]] for k in range(len(final_id))]
print(tabulate(table))

