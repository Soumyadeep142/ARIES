import numpy as np
ID = np.loadtxt('refstars_new.list', unpack = True, usecols = (0))
RA, DEC = np.loadtxt('refstars_new.list', unpack = True, usecols = (3, 4), dtype = str)
final_id, period = np.loadtxt('Final_Period.txt', unpack = True, usecols = (0, 1))
ra_list = []
dec_list = []
period_list = []
for j in range(len(ID)):
    ID[j] = int(ID[j])
    #print(type(ID[j]))
    for i in range(len(final_id)):
        final_id[i] = int(final_id[i])
        #print(type(i))
        if final_id[i] == ID[j]:
            r = RA[j]
            d = DEC[j]
            p = period[i]
            ra_list.append(r)
            dec_list.append(d)
            period_list.append(round(p, 5))


final_id, ra_list, dec_list, period_list = zip(*sorted(zip(final_id, ra_list, dec_list, period_list)))
print(len(ra_list), len(dec_list), len(period_list))
data = np.column_stack((final_id, ra_list, dec_list, period_list))
np.savetxt('Final_RA_DEC_Period.txt', data, fmt = '%s')


