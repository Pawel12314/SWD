import pandas as pd
def loadDT(filename,sep,dec):
    return pd.read_csv(filename,sep=sep,decimal=dec,header=0,engine ='python')