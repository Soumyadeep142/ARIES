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
print("Final number of stars:", len(all_files))

id = []
files = []

for k in range(len(all_files)):
    popped_id = all_files[k].pop(0)
    id.append(popped_id)
    files.append(all_files[k])

d = {}
for i in range(len(id)):
    d[id[i]] = files[i]
#print(d)

df = pd.DataFrame.from_dict(d, orient = 'index')

print(df.head)


df.to_csv('stars_reduced.csv')
print('csv saved')





'''    

#id is a list of ids of required stars and files is a list of .std files which contain those stars
#stacking them together
data = np.column_stack((id, files))

#saving it as a .txt file
np.savetxt('stars_reduced.txt', data, fmt = '%s')
print('Final file saved')
'''
