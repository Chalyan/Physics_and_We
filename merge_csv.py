import numpy as np
import pandas as pd
import os 

dirpath = '/Users/eduard/Projects/Physics_and_We/pandw'
files = np.array([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])

wl = pd.read_csv(f'{dirpath}//{files[0]}', skiprows=1).iloc[:,0]
values = np.zeros((wl.shape[0],len(files)))

for i in range(len(files)):
    values[:,i] = pd.read_csv(f'{dirpath}//{files[i]}', skiprows=1).iloc[:,1]

df = pd.DataFrame(values, columns=files)
print(df)
