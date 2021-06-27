import numpy as np
import glob
import math
import pandas as pd
#List of all .std files
std_files = [f for f in glob.glob("*.std")]
#Loading reference file
id_ref, x_ref, y_ref = np.loadtxt('refstars_new.list', unpack = True, usecols = (0, 1, 2))
#Loading second cut file
id_sc = np.loadtxt('Second cut.txt', unpack = True, usecols = (0))


id_dict = {}
for i in id_sc:
    id_dict[i] = []

c = 1
for std in std_files:
    std_id, std_x, std_y, std_e = np.loadtxt(std, skiprows = 3, usecols = (0, 1, 2, 4), unpack = True)
    print(f'working for file {c}: {std}')
    for (i, x, y, e) in zip(std_id, std_x, std_y, std_e):
        if e < 0.05:
            for n in id_sc:
                pos = np.where(id_ref == n)
                x1 = x_ref[pos].item()
                y1 = y_ref[pos].item()
                d = math.dist([x, y], [x1, y1])
                if d <= 2:
                    id_dict[n].append(std_id)
                    break
                else:
                    id_dict[n].append(-1)

    c += 1

df = pd.DataFrame.from_dict(id_dict, orient = 'index', columns = std_files)
df.to_csv('matching_IDs.csv')
print('csv saved')





