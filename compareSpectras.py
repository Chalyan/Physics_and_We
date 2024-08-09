import numpy as np
import numpy.linalg as nl
import os
import srcread

src = srcread.SRCRead('/Users/eduard/Projects/Physics_and_We/source.txt')
dirpath = src.findPath('measurments_folder')
files = np.array([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])

def orthoNormalizeVectorSet(vectors):

    e_basis = []
    norms = []

    for i in range(len(vectors)):
        current = vectors[i]
        
        for j in range(i):
            e_j = e_basis[j]
            current -= np.dot(current, e_j) * e_j
        norms.append(nl.norm(current))
        
        if nl.norm(current) != 0:
            current /= nl.norm(current)

        e_basis.append(current)
    
    coff = []
    
    for i in range (len(vectors)):
        coff.append([])
        for j in range (len(vectors)):
            summ = 0
            if j<i or norms[j] == 0:
                coff[i].append(0)
            elif j==i:
                coff[i].append(1/norms[j])
            elif j>i:
                for k in range(j):
                    summ -= (np.dot(vectors[j],e_basis[k])*coff[i][k])
                summ = summ/norms[j]
                coff[i].append(summ)
    
    return e_basis, coff


def evaluateSolution(B, vectors):

    basis, coeffs = orthoNormalizeVectorSet(vectors)

    B1 = []

    for i in range(len(vectors)):
        B1.append(np.dot(B, basis[i]))
    
    X = []

    blueX = 0
    redX = 0

    for i in range(len(vectors)):
        X.append(np.dot(B1, coeffs[i]))
        file1 = files[i].split('.')[0]
        s = file1.split('_')[2]
        if 'inkb' in file1:
            blueX += X[i] * int(s[0:s.find('d')]) * 0.023
        elif 'inkr' in file1:
            redX += X[i] * int(s[0:s.find('d')]) * 0.023
    
    xsum = sum(X) 

    blue, red = blueX/xsum, redX/xsum

   # return f"Blue: {blue}\nRed: {red}"
    return blue, red
