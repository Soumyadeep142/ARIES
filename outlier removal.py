import numpy as np
import glob
#List of all .std files
std_files = [f for f in glob.glob("*.std")]
#Loading first cut data file
id, avg_mag_col, SD_col = np.loadtxt('second_cut_5.txt', usecols = (0, 1, 2), unpack = True)

#Initializing dictionaries to store list of magnitudes and files corresponding to each ID
#NOTE: These dictionaries store data for all IDs before the second cut
mag_dict = {}
files_dict = {}
err_dict = {}
for j in id:
    mag_dict[j] = []
    files_dict[j] = []
    err_dict[j] = []

for std in std_files:
    std_id, std_mag, std_err = np.loadtxt(std, skiprows = 3, usecols = (0, 3, 4), unpack = True)
    for i in range(len(id)):
        if id[i] in std_id:
            avg = avg_mag_col[i]
            SD = SD_col[i]
            pos = np.where(std_id == id[i])
            m = std_mag[pos].item()
            e = std_err[pos].item()
            if m >= (avg - 3 * SD) and m <= (avg + 3 * SD):
                mag_dict[id[i]].append(m)
                files_dict[id[i]].append(std)
                err_dict[id[i]].append(e)


#List of IDs of reduced number of stars after second cut
reduced_id = []
for i in id:
    if len(files_dict[i]) / len(std_files) > 0.25:
        reduced_id.append(i)

print('Number of stars after second cut:', len(reduced_id))

#Lists to store average magnitude and standard deviation of reduced number of stars after second cut
avg_mag_list = []
SD_list = []
mean_err_list = []
quadrature = []
for i in reduced_id:
    avg_m = np.mean(mag_dict[i])
    SD_m = np.std(mag_dict[i])
    err_m = np.mean(err_dict[i])
    a = (np.sqrt(sum(np.square(err_dict[i]))) / len(err_dict[i]))
    avg_mag_list.append(avg_m)
    SD_list.append(SD_m)
    mean_err_list.append(err_m)
    quadrature.append(a)


'''
arr = np.column_stack((reduced_id, avg_mag_list, SD_list))
np.savetxt('second_cut_6.txt', arr, fmt = '%s')
print('file saved')
'''
