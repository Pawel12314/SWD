import pandas as pd
import numpy as np
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import math
def toNumeric(df,col):
    unique=df[col].str.upper().unique()
    print(unique)
    df[col].replace(unique,range(len(unique)), inplace=True)
    return df
def toDiscrete(df,step,col):
    max=df.max(axis=0)[col]
    min=df.min(axis=0)[col]
    df[col] = df[col].astype(float)
    df[col] = pd.cut(x=df[col],bins=np.arange(min,max,step))
    return df
def normalize(df,col):
    stdev=df[col].std()
    mean= df[col].mean()
    df[col]=(df[col]-mean)/stdev
    return df
def changeRange(df,col,newa,newb):
    max = df.max(axis=0)[col]
    min = df.min(axis=0)[col]
    df[col] = ((newb-newa)/(max-min))*(df[col]-min)+newa
    return df
def findLessThan(df, col, threshold):
    d1=df.sort_values(by=[col],ascending=True)
    num=len(df.iloc[:,0])*(threshold/100.0)
    print(str(int(num)))
    return d1.head(int(num))
def findGreaterThan(df, col, threshold):
    d1=df.sort_values(by=[col],ascending=False)
    num = len(df.iloc[:, 0]) * (threshold / 100.0)
    return d1.head(int(num))

def CellEuclideanDistance(val1,val2):
    return pow(val1-val2,2)
def RowEuclideanDistance(row1,row2):
    range1 = range(len(row1))
def EuclideanDistance(current,dataframe,n):
    r=range(len(dataframe.iloc[:,0]))
    reslist={}
    for i in r:
        res=0
        for col in  dataframe.columns.values.tolist():
            if is_numeric_dtype(dataframe[col]):
                #print(dataframe.iloc[i][col])
                #print(current[col])
                res = res + pow(dataframe.iloc[i][col]-current[col],2)
        res = math.sqrt(res)
        cols=dataframe.columns.values.tolist()
        dec=cols[len(cols)-1]

        reslist[i]=[dataframe.iloc[i][dec],res]

    #print(reslist)
    res1={k: v for k, v in sorted(reslist.items(), key=lambda item: item[1][1])[1:n+1]}
    #print(res1)
    return res1
def kfold(instance,dataframe,k,n,T):
   # correctclass = instance[-1]
    #print(correctclass)
    #return
    cnt = len(dataframe.iloc[:, 0])
    div=int(cnt/k)
    res=[]
    for i in range(k):

        lim=div*i
        p1=dataframe.iloc[0:lim,:]
        p2=dataframe.iloc[lim+div:cnt,:]
        px=dataframe.iloc[lim+1:lim+div-1,:]
        frames = [p1, p2]
        result = pd.concat(frames)
        result = result.reset_index()
        result=result.drop(result.columns[[0]], axis=1)
        iter=0
        #print(str(len(px.iloc[:,0])))
        kfolded=[]
        sum=0
        for rowiter in range(len(px.iloc[:,0])):
            knn=EuclideanDistance(px.iloc[rowiter,:],dataframe,n)
            class1={}
            #print("knn ",knn)
            for res1 in knn:
                tmp=str(knn[res1][0])
                #print("neigbour ",tmp)
                if knn[res1][0] in class1:
                    class1[tmp] = class1[tmp] + 1
                else:
                    class1[tmp] = 1
                #print(knn[res1][0])
                #print(knn[res1][1])
                #print("---")
            #print(class1)
            #print(knn)
            #print(type(knn))
            #print(class1)

            row=px.iloc[rowiter,:]
            correctclass = str(row[-1])
            if correctclass in class1:
                if float(class1[correctclass])/float(n)>T:
                    sum = sum+1
                    #print(class1[correctclass])
                    #print(class1[correctclass]/n)
            kfolded.append([{"class ": class1}, {"correctclass": correctclass}])
        limupper=lim+div-1
        s=str(lim)+" "+str(limupper)
        res.append([{"kfold":kfolded},{"sum":sum},{"range",s}])
        #print("kfolded",kfolded)
    for item in res:
        print(item[1]," ",div," ",item[2])
    #print(res)
    return res