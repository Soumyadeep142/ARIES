import numpy as np
time, mag = np.loadtxt(r"C:\Users\dell\Downloads\541-1842_with_outliers.txt", unpack = True, skiprows = 1, usecols = (0, 1), delimiter = ',')
print(len(mag))

#Removing outliers
for i in range(3):
    mean_mag = np.mean(mag)
    SD_mag = np.std(mag)
    final_mag = []
    final_time = []
    for (m, t) in zip(mag, time):
        if m >= mean_mag - 3 * SD_mag and m <= mean_mag + 3 * SD_mag:
            final_mag.append(m)
            final_time.append(t)
    mag = final_mag
    time = final_time

print(len(mag))
#Removing sudden change
'''
t1 = time[1]
t0 = time[0]
m1 = mag[1]
m0 = mag[0]
time_new_list = []
mag_new_list = []
'''
j = 0
while j < len(mag) - 1:
    l = len(mag)
    if np.floor(time[j + 1]) - np.floor(time[j]) == 0.0 and np.abs(mag[j + 1] - mag[j]) > 0.3:
        time.pop(j + 1)
        mag.pop(j + 1)

    elif np.floor(time[j + 1]) - np.floor(time[j]) == 1.0 and np.abs(mag[j + 1] - mag[j]) > 0.5:
        time.pop(j + 1)
        mag.pop(j + 1)

    elif np.floor(time[j + 1]) - np.floor(time[j]) > 1.0 and np.abs(mag[j + 1] - mag[j]) > 0.6:
        time.pop(j + 1)
        mag.pop(j + 1)

    l1 = len(mag)
    if l == l1:
        j = j + 1
    else:
        j = j

print(len(mag))

data = np.column_stack((time, mag))
np.savetxt('test_file.txt', data, fmt = '%s')