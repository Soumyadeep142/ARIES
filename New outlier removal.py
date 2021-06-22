import numpy as np
import glob
import math
import pandas as pd

#List of all .std files
std_files = [f for f in glob.glob("*.std")]
#Loading reference file
id_ref, x_ref, y_ref = np.loadtxt('refstars_new.list', usecols = (0, 1, 2), unpack = True)
a = 1
for k in range(3):
    print(f'ITERATION: {a}')
    #Loading first cut data file
    id, avg_mag_col, SD_col = np.loadtxt('second_cut.txt', usecols = (0, 1, 2), unpack = True)

    #Initializing dictionaries to store list of magnitudes and files corresponding to each ID
    #NOTE: These dictionaries store data for all IDs before the second cut
    mag_dict = {}
    files_dict = {}
    err_dict = {}
    for j in id:
        mag_dict[j] = []
        files_dict[j] = []
        err_dict[j] = []

    c = 1
    for std in std_files:
        std_x, std_y, std_m, std_e = np.loadtxt(std, skiprows = 3, usecols = (1, 2, 3, 4), unpack = True)
        print(f'checking for file {c}: {std}')
        for (x, y, m, e) in zip(std_x, std_y, std_m, std_e):
            if e < 0.05:
                for i in range(len(id)):
                    avg = avg_mag_col[i]
                    SD = SD_col[i]
                    pos = np.where(id_ref == id[i])
                    x1 = x_ref[pos].item()
                    y1 = y_ref[pos].item()
                    d = math.dist([x, y], [x1, y1])
                    if d <= 2:
                        if m >= (avg - 3 * SD) and m <= (avg + 3 * SD):
                            mag_dict[id[i]].append(m)
                            files_dict[id[i]].append(std)
                            err_dict[id[i]].append(e)
        c += 1

    #List of IDs of reduced number of stars after second cut
    reduced_id = []
    for i in id:
        if len(files_dict[i]) / len(std_files) > 0.25:
            reduced_id.append(i)

    print(f'Number of stars after second cut iteration {a}:', len(reduced_id))

    #Lists to store average magnitude and standard deviation of reduced number of stars after second cut
    avg_mag_list = []
    SD_list = []
    avg_err_list = []
    final_files = {}
    for i in reduced_id:
        avg_m = np.mean(mag_dict[i])
        SD_m = np.std(mag_dict[i])
        err_m = np.mean(err_dict[i])
        avg_mag_list.append(avg_m)
        SD_list.append(SD_m)
        avg_err_list.append(err_m)
        final_files[i] = files_dict[i]

    df = pd.DataFrame.from_dict(final_files, orient = 'index')
    df.to_csv('second_cut_stars_with_files.csv')
    print('csv saved')

    data = np.column_stack((reduced_id, avg_mag_list, SD_list, avg_err_list))
    np.savetxt('second_cut.txt', data, fmt = '%s')
    print('second cut txt file saved')
    a += 1
