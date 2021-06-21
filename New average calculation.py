import numpy as np
import glob
import math
id, x_ref, y_ref = np.loadtxt('refstars_new.list', usecols=(0, 1, 2), unpack='True')
std_files = [f for f in glob.glob("*.std")]

'''
def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
'''


mag_dict = {}
err_dict = {}
for i in id:
    mag_dict[i] = []
    err_dict[i] = []
c = 1
for std in std_files:
    std_x, std_y, std_m, std_e = np.loadtxt(std, skiprows = 3, usecols = (1, 2, 3, 4), unpack = True)
    print(f'checking for file {c}')
    for (x, y, m, e) in zip(std_x, std_y, std_m, std_e):
        for n in range(22066):
            d = math.dist([x, y], [x_ref[n], y_ref[n]])
            if d <= 2:
                mag_dict[n + 1].append(m)
                err_dict[n + 1].append(e)
                break

    c += 1


avg_mag = []
avg_err = []
for i in id:
    avg_m = np.mean(mag_dict[i])
    avg_e = np.mean(err_dict[i])
    avg_mag.append(avg_m)
    avg_err.append(avg_e)

data = np.column_stack((id, avg_mag, avg_err))
np.savetxt('new_avg_mag_error.txt', data, fmt='%s')
