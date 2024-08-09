# import Merging_CSV_files

# Merging_CSV_files.mergeCSVfiles()

import compareSpectras
import extractSpectras
import pandas as pd

dfB = pd.read_csv('/Users/eduard/Projects/Physics_and_We/pandw/inkb_100ms_7d.csv', skiprows=1)

b = dfB.iloc[472:1158,1].values.tolist()
vectors = extractSpectras.getVectors()

coef1, coef2 = compareSpectras.evaluateSolution(b, vectors)
print(type(vectors[0][0]))
# print(coef1 * list(vectors[0]))
