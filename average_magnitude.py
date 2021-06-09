import pandas as pd
import numpy as np

df = pd.read_csv('stars_reduced.csv', dtype = object)
df.set_index('id', inplace = True)

id_points = []
mag_points = []

for id in df.index:
    print('ID:', id)
    magnitude = 0
    files = df.loc[id]
    for j in files:
        #print('checking file ', j, 'for ID ', id)
        if pd.isna(j):
            #print('no file, wont check')
            pass
        else:
            identity, mag = np.loadtxt(j, skiprows = 3, usecols = (0, 3), unpack = True)
            #print('loaded file', j, 'for ID:', id)
            for i in range(len(identity)):
                if str(int(identity[i])) == str(id):
                    #print('ID matched')
                    magnitude += mag[i]
                    break
    avg_mag = magnitude / len(files)
    print('avg magnitude for ID ', id, 'is', avg_mag)
    id_points.append(id)
    mag_points.append(avg_mag)

print(id_points)
print(mag_points)

A = np.column_stack((id_points, mag_points))

data = pd.DataFrame(A, columns = ['ID', 'Average Magnitude'])

data.to_csv('avg_magnitude.csv')
print('csv file saved')







