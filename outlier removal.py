import numpy as np
import glob
#List of all .std files
std_files = [f for f in glob.glob("*.std")]
#Loading first cut data file
id, avg_mag_col, SD_col = np.loadtxt('Avg_Mag_and_SD.txt', usecols = (0, 1, 2), unpack = True)

#Initializing dictionaries to store list of magnitudes and files corresponding to each ID
#NOTE: These dictionaries store data for all IDs before the second cut
mag_dict = {}
files_dict = {}
for j in id:
    mag_dict[j] = []
    files_dict[j] = []

for std in std_files:
    std_id, std_mag = np.loadtxt(std, skiprows = 3, usecols = (0, 3), unpack = True)
    for i in range(len(id)):
        if id[i] in std_id:
            avg = avg_mag_col[i]
            SD = SD_col[i]
            pos = np.where(std_id == id[i])
            m = std_mag[pos].item()
            if m >= (avg - 3 * SD) and m <= (avg + 3 * SD):
                mag_dict[id[i]].append(m)
                files_dict[id[i]].append(std)

#List of IDs of reduced number of stars after second cut
reduced_id = []
for i in id:
    if len(files_dict[i]) / len(std_files) > 0.25:
        reduced_id.append(i)

print('Number of stars after second cut:', len(reduced_id))

#Lists to store average magnitude and standard deviation of reduced number of stars after second cut
avg_mag_list = []
SD_list = []
for i in reduced_id:
    avg_m = np.mean(mag_dict[i])
    SD_m = np.std(mag_dict[i])
    avg_mag_list.append(avg_m)
    SD_list.append(SD_m)

arr = np.column_stack((reduced_id, avg_mag_list, SD_list))
np.savetxt('second_cut_data.txt', arr, fmt = '%s')
print('file saved')
