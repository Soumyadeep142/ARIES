import numpy as np
time, mag = np.loadtxt(r"C:\Users\dell\Downloads\541-1842_with_outliers.txt", unpack = True, skiprows = 1, usecols = (0, 1), delimiter = ',')

#Removing outliers
for i in range(3):
    mean_mag = np.mean(mag)
    SD_mag = np.std(mag)
    final_mag = []
    final_time = []
    for (m, t) in zip(mag, time):
        if m >= mean_mag - 2 * SD_mag and m <= mean_mag + 2 * SD_mag:
            final_mag.append(m)
            final_time.append(t)
    mag = final_mag
    time = final_time

#Removing sudden change
j = 1
t1 = time[1]
t0 = time[0]
m1 = mag[1]
m0 = mag[0]

time_new_list = []
mag_new_list = []
while j < len(time) - 2:
    if ((t1 - t0) <= 0.00347):
        if abs(m1 - m0) > 0.3:
            time_new_list.append(t0)
            mag_new_list.append(m0)
            t0 = t0
            m0 = m0
        else:
            time_new_list.append(t0)
            mag_new_list.append(m0)
            t0 = t1
            m0 = m1
    elif ((t1 - t0) <= 1):
        if abs(m1 - m0) > 0.4:
            time_new_list.append(t0)
            mag_new_list.append(m0)
            t0 = t0
            m0 = m0
        else:
            time_new_list.append(t0)
            mag_new_list.append(m0)
            t0 = t1
            m0 = m1

    elif abs(m1 - m0) > 0.5:
        time_new_list.append(t0)
        mag_new_list.append(m0)
        t0 = t0
        m0 = m0

    else:
        time_new_list.append(t0)
        mag_new_list.append(m0)
        t0 = t1
        m0 = m1
    t1 = time[j + 1]
    m1 = mag[j + 1]
    j = j + 1

data = np.column_stack((time_new_list, mag_new_list))
np.savetxt('test_file.txt', data, fmt = '%s')