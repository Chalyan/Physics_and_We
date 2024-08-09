import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plt_multy(wl, X, ax):
    for i in X.values:
       ax.plot(wl, i)
    ax.legend(X.index)

def to_df(path, files, group):
    data = {}
    for f in files[group]:
        name = f.split('.')[0]
        P = pd.read_csv(f'{path}/{f}', header=None, skiprows=2, usecols=[1],
                        names=[name.split('_')[2] if len(name.split('_')) > 2 else 0])
        data[name] = P

    df = pd.concat(data.values(), axis=1)
    return df.T

def get(data, group):

    P = data.get_group((group,)).iloc[:, 1:]

    return P

def dist(X, y):

     return (np.sqrt(((X - y)**2).sum(axis=1))).sum()

def mean_norm(X):
    X_normalized = (X - X.min()) / (X.max() - X.min())
    return X_normalized

def std_norm(X):
    X_norm = (X - X.mean()) / X.std()
    return X_norm

def p_idx(y):

    return np.where(y == y.max())