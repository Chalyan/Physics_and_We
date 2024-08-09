from db import *
import matplotlib.pyplot as plt
import numpy as np
from func import *


#plt_multy(wl, BLUE)
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax.scatter(peak_r, C)
ax.plot(peak_r, fit_r(peak_r))
ax.scatter(R, fit_r(R))

ax1 = fig.add_subplot(2, 2, 2)
ax1.scatter(peak_b, C)
ax1.plot(peak_b, fit_b(peak_b))
ax1.scatter(R, fit_b(R))

ax2 = fig.add_subplot(2, 1, 2)
plt_multy(wl, BLUE, ax2)

plt.show()

