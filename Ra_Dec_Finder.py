import numpy as np
ID = np.loadtxt('refstars_new.list', unpack = True, usecols = (0))
RA, DEC = np.loadtxt('refstars_new.list', unpack = True, usecols = (3, 4), dtype = str)
final_id = np.loadtxt('Final_Period.txt', unpack = True, usecols = (0))
ra_list = []
dec_list = []
for j in range(len(ID)):
    ID[j] = int(ID[j])
    #print(type(ID[j]))
    for i in final_id:
        i = int(i)
        #print(type(i))
        if i == ID[j]:
            print('matched')
            r = RA[j]
            d = DEC[j]
            ra_list.append(r)
            dec_list.append(d)


print(len(ra_list), len(dec_list))
data = np.column_stack((final_id, ra_list, dec_list))
np.savetxt('Final_RA_DEC.txt', data, fmt = '%s')


