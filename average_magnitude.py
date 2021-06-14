import numpy as np
import glob
import pandas as pd
#List of all .std files
std_files = [f for f in glob.glob("*.std")]
#Loading reference file
ID, x_ref, y_ref = np.loadtxt('refstars_new.list', usecols = (0, 1, 2), unpack = True)
#Number of total stars
stars = len(ID)
#Each element (list) in array A stores id and paths of all .std files where it finds that star (in a single list)

A = []

for i in range(stars):
    A.append([ID[i]])


for std in std_files:
    std_id = np.loadtxt(std, skiprows = 3, usecols = (0), unpack = True)
    for j in std_id:
        if j in ID:
            A[int(j)-1].append(std)
print("std files uploaded")

#all_files will contains (same as A) about the stars which are present in more than 25% frames
all_files = []

for k in range(stars):
    if(len(A[k]) - 1) / len(std_files) > 0.25:
        all_files.append(A[k])
#print("Final number of stars:", len(all_files))

id = []
files = []

for k in range(len(all_files)):
    popped_id = all_files[k].pop(0)
    id.append(popped_id)
    files.append(all_files[k])
#print("Number of stars", len(l))

#print(id)
print("Final number of stars ", len(id))
d = {}
for i in range(len(id)):
    d[id[i]] = files[i]
#print(d)


df = pd.DataFrame.from_dict(d, orient = 'index')

#print(df.head)


df.to_csv('stars_reduced.csv')
print('csv saved')

'''
np.savetxt('Final IDs', id)
print('Final IDs saved')
'''

'''    

#id is a list of ids of required stars and files is a list of .std files which contain those stars
#stacking them together
data = np.column_stack((id, files))

#saving it as a .txt file
np.savetxt('stars_reduced.txt', data, fmt = '%s')
print('Final file saved')
'''

#CODE FOR AVERAGE MAGNITUDE CALCULATION

#Initializing dictionary that stores ID wise sum of magnitudes across all files
#Initializing another dictionary that stores magnitudes of all observations of an ID in a list
mag_sum = {}
magnitudes = {}
for i in id:
    mag_sum[i] = 0
    magnitudes[i] = []

#Calculating sum of magnitudes of an ID by adding magnitudes from each frame
for std in std_files:
    std_id, std_mag = np.loadtxt(std, skiprows = 3, usecols = (0, 3), unpack = True)
    #print('Loaded file', std)
    for i in id:
        if i in std_id:
            #print('ID matched', i, 'in', std)
            pos = np.where(std_id == i)
            mag_sum[i] += std_mag[pos].item()
            magnitudes[i].append(std_mag[pos].item())
            #print(mag_sum)

print(magnitudes)
print('Number of mags for first id', len(magnitudes[3]))
#Initializing dictionary to store ID wise average magnitude
avg_mag= {}
for i in id:
    #print('ID: ', i)
    avg_mag[i] = mag_sum[i] / len(d[i])
    #print('Average magnitude of ID', i , 'is', avg_mag[i])


avg_mag_list = []
#Initializing a list. Each component of this list will be a list containing all magnitudes of a particular ID.
mag_list = []
for i in id:
    avg_mag_list.append(avg_mag[i])
    mag_list.append(magnitudes[i])

#Initializing a list to store standard deviation of a particular ID
SD_mag = []
for i in mag_list:
    SD_mag.append(np.std(i))


arr = np.column_stack((id, avg_mag_list, SD_mag))
np.savetxt('Avg_Mag_and_SD.txt', arr, fmt= '%s')
print('Average magnitudes and SD .txt file saved')


data = pd.DataFrame(list(zip(id, avg_mag_list, SD_mag)))
data.to_csv('Avg_Mag_and_SD.csv')
print('Average magnitudes and SD csv file saved')


    



