from sympy import *
# import qgrid
import matplotlib.pyplot as plt
# from pandasgui.datasets import titanic
import Gui as gui

import Api as api
import dataAcess as data
import pandas as pd
# df=data.loadDT(r"D:\nauka\tylkoStudia\magisterium2\systemy_wspomagania_decyzji\dt\INCOME2.txt",'\t', ",")


def ReadFromConsole():
    x= input()
    print(x)
    return x
def readSeparator():
    print("type column separator here")
    return input()
def readDecimalLimiter():
    print("type decimal separator here")
    return input()
def readDT():
    print("""write data file name""")
    datafile = input()
    declimiter=readDecimalLimiter()
    sep=readSeparator()
    df = data.loadDT(datafile,sep, declimiter)
    #gui.showDt(df)
    return df
def naNumeryczne(df):
    print("type column name")
    colname=ReadFromConsole()
    newdf = api.toNumeric(df, colname)
    #gui.showDt(newdf)
    return newdf
def dyskretyzacja(df):
    print("type column name")
    colname=input()
    print("print discretization step")
    step=float(input())
    newdf = api.toDiscrete(df, col=colname, step=step)
    #gui.showDt(newdf)
    return newdf
def normalizacja(df):
    print("type column name")
    colname=input()
    newdf =  api.normalize(df,colname)
    #gui.showDt(newdf)
    return newdf
def zmienzakres(df):
    print("type column name")
    colname=input()
    print("type minimum value")
    min=float(input())
    print("type maximum value")
    max=float(input())
    newdf = api.changeRange(df,colname,min,max)
    #gui.showDt(newdf)
    return newdf
def getgreaterthan(df):
    print("type column name")
    colname=input()
    print("type greater than threshold")
    t=float(input())
    newdf = api.findGreaterThan(df,colname,t)
    #gui.showDt(newdf)
    return newdf
def getlessthan(df):
    print("type column name")
    colname=input()
    print("type lower than threshold")
    t=float(input())
    newdf = api.findLessThan(df,colname,t)
    #gui.showDt(newdf)
    return newdf
def getPlot2d(df):
    print("type first column name")
    colname1=input()
    print("type second column name")
    colname2=input()
    gui.plot2d(df, colname1, colname2)
def getPlot3d(df):
    print("type first column name")
    colname1 = input()
    print("type second column name")
    colname2 = input()
    print("type third column name")
    colname3 = input()
    gui.plot2d(df, colname1, colname2,colname3)
def getHistogram(df):
    print("type column name")
    colname=input()
    print("type num classes -> (-1) is default value")
    classcount=input()
    gui.histogram(df, colname, classcount)
def show(df):
    gui.showDt(df)
def KNN(df):
    print("type row number")
    rownr = int(input())
    print("type neibourgh number")
    k = int(input())
    print("type fold number")
    n= int(input())
    print("type correct result threshold")
    T = float(input())
    api.kfold(df.iloc[rownr], df, k, n, T)
def loop(df=None):

    msg="""
    1 - read dataset
    2 - convert text data to numeric
    3 - discretize
    4 - normalization
    5 - range change
    6 - select n% lowest values
    7 - select n% highest values
    8 - 2d plot
    9 - 3d plot
    10 - histogram
    11 - display data
    12 - run KNN algorithm
    """
    print(msg)
    data1 = input()
    if data1 == "1":
        df=readDT()
        return df
    elif df.empty is  None:
        print("dataframe was not loaded")
        return None
    elif data1 == "2":
        return naNumeryczne(df)
    elif data1 == "3":
        print("is 3")
        return dyskretyzacja(df)
    elif data1 == "4":
        return normalizacja(df)
    elif data1 == "5":
        return zmienzakres(df)
    elif data1 == "6":
        return getlessthan(df)
    elif data1 == "7":
        return getgreaterthan(df)
    elif data1 == "8":
        getPlot2d(df)
        return df
    elif data1 == "9":
        getPlot3d(df)
        return df
    elif data1 == "10":
        return getHistogram(df)
    elif data1 == "11":
        show(df)
        return df
    elif data1 == "12":
        KNN(df)
        return df
    else:
        print("podano nieprawidłowe dane")