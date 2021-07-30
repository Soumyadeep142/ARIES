import numpy as np
import glob
import math
import pandas as pd
#List of all .std files
std_files = [f for f in glob.glob("*.std")]

#Loading reference file
id_ref, x_ref, y_ref = np.loadtxt('refstars_new.list', unpack = True, usecols = (0, 1, 2))
#Loading second cut file
id_sc = np.loadtxt('Second_cut.txt', unpack = True, usecols = (0))


id_dict = {}
for i in id_sc:
    id_dict[i] = [-1] * len(std_files)

c = 0
for std in std_files:
    std_id, std_x, std_y, std_mag, std_e = np.loadtxt(std, skiprows = 3, usecols = (0, 1, 2, 3, 4), unpack = True)
    print(f'working for file {c+1}: {std} {len(std_x)}')
    for n in id_sc:
        pos = np.where(id_ref == n)
        x1 = x_ref[pos].item()
        y1 = y_ref[pos].item()
        for (i, x, y, m, e) in zip(std_id, std_x, std_y, std_mag, std_e):
            d = math.dist([x, y], [x1, y1])
            if d <= 2:
                id_dict[n][c] = m
                break
            #else:
                #id_dict[n].append(-1)
                #break

    c += 1

df = pd.DataFrame.from_dict(id_dict, orient = 'index', columns = std_files)
df.to_csv('matching_mags.csv')
print('csv saved')
