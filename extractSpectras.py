import pandas as pd
import srcread

reader = srcread.SRCRead('/Users/eduard/Projects/Physics_and_We/source.txt')
spectras_csv_path = reader.findPath('spectras_csv_path')[:-1]

def getVectors():
    
    df = pd.read_csv(spectras_csv_path, skiprows=1)
    start = 472
    end = 1158

    vectors = df.values[472:1158,1:].T
    vectors = vectors.tolist()   
    
    
    return vectors
