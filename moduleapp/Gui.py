from pandasgui import show
import matplotlib.pyplot as plt
import math
def showDt(dt):
    show(dt)

def plot2d(df,col1,col2):
    plt.scatter(df[col1],df[col2])
    plt.show()
    return
def plot3d(df,col1,col2,col3):
    ax = plt.axes(projection="3d")
    ax.scatter3D(df[col1],df[col2],df[col3])
    #ax.axis([-2,2,-2,2])
    plt.show()
    return
def histogram(df,col,num):
    if num==-1:
        num = math.sqrt(df.shape[0])
        num = math.floor(num)
    df.hist(column=col,bins=num)
    plt.show()