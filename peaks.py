import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

df = pd.read_csv('fluorescence.csv', skiprows = 91)
x = df.iloc[:,0]
a = df.shape[1]



for column in range(a-1):
    y = df.iloc[:,column+1]
    plt.plot(x,y)
    peaks, _ = find_peaks(y)
    peak_x_values = x[peaks]
    peak_y_values = y[peaks]
    plt.scatter(peak_x_values, peak_y_values, s=50)
 
  
for i in range(len(peaks)):
    
    if  x[i] >= 515 and x[i] <= 525:
        print("red")

    if  x[i] >= 625 and x[i] <= 635:
        print("blue")
   
   


print(peak_x_values)
print(peak_y_values)

plt.xlabel('Wavelength')
plt.ylabel('Intesity')

plt.show()


