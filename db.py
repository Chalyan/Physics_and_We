import os
import pandas as pd
import numpy as np
#import srcread
from func import *

#sourcePaths = srcread.SRCRead('/Users/eduard/Projects/Physics_and_We/source.txt')

folder_path = '/Users/eduard/Projects/Physics_and_We/files'  # Update with your folder path
files = np.array([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
files.sort()
print(files)
wl = pd.read_csv(f'{folder_path}//{files[0]}', skiprows=1).iloc[:,0]
values = np.zeros((wl.shape[0],len(files)))

for i in range(len(files)):
    values[:,i] = pd.read_csv(folder_path+'/'+files[i], skiprows=1).iloc[:,1]

df = pd.DataFrame(values, columns=files)

red_ix = np.array([1 if 'inkr' in filename else 0 for filename in files]).astype('bool')
blue_ix = np.array([1 if 'inkb' in filename else 0 for filename in files]).astype('bool')

a = 472#472
b = 1158#1158

wl = wl[a:b]
BLUE = to_df(folder_path, files, blue_ix).iloc[:, [*range(a, b)]]
RED = to_df(folder_path, files, red_ix).iloc[:, [*range(a, b)]]

blue, red = BLUE.values, RED.values
spec_x = pd.read_csv(f'{folder_path}/purple_100ms.csv', skiprows=1, usecols=[1]).values.T[0][a:b]

C = np.arange(1, 11) * 0.023 #267, 514


peak_b = blue[:, 514]
peak_r = red[:, 267]

coef_r = np.polyfit(peak_r,C,1)
coef_b = np.polyfit(peak_b,C,1)

fit_r = np.poly1d(coef_r)
fit_b = np.poly1d(coef_b)
R, B = spec_x[[267, 514]]

print(f"R: {fit_r(R)} ml, B: {fit_b(B)} ml")
