import numpy as np
import glob
import math
import pandas as pd
id, x_ref, y_ref = np.loadtxt('refstars_new.list', usecols = (0, 1, 2), unpack = True)
std_files = [f for f in glob.glob("*.std")]

'''
def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
'''

mag_dict = {}
err_dict = {}
files_dict = {}
for i in id:
    mag_dict[i] = []
    err_dict[i] = []
    files_dict[i] = []

c = 1
for std in std_files:
    std_x, std_y, std_m, std_e = np.loadtxt(std, skiprows = 3, usecols = (1, 2, 3, 4), unpack = True)
    print(f'checking for file {c}')
    for (x, y, m, e) in zip(std_x, std_y, std_m, std_e):
        for n in range(22067):
            d = math.dist([x, y], [x_ref[n], y_ref[n]])
            if d <= 2:
                mag_dict[n + 1].append(m)
                err_dict[n + 1].append(e)
                files_dict[n + 1].append(std)
                break

    c += 1

final_id = []
for i in id:
    if (len(files_dict[i]) / len(std_files)) > 0.25:
        final_id.append(i)

print('25% condition check completed')
print('Number of stars after first cut', len(final_id))

final_files = {}
avg_mag = []
avg_err = []
for i in final_id:
    avg_m = np.mean(mag_dict[i])
    avg_e = np.mean(err_dict[i])
    avg_mag.append(avg_m)
    avg_err.append(avg_e)
    final_files[i] = files_dict[i]

df = pd.DataFrame.from_dict(final_files, orient = 'index')
df.to_csv('stars_with_files.csv')
print('csv saved')


data = np.column_stack((final_id, avg_mag, avg_err))
np.savetxt('new_avg_mag_error.txt', data, fmt='%s')
print('txt file saved')
