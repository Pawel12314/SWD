from sympy import *
# import qgrid
import matplotlib.pyplot as plt
# from pandasgui.datasets import titanic
import Gui as gui

import Api as api
import dataAcess as data

# df=data.loadDT(r"D:\nauka\tylkoStudia\magisterium2\systemy_wspomagania_decyzji\dt\INCOME2.txt",'\t', ",")
df = data.loadDT(r"D:\nauka\tylkoStudia\magisterium2\systemy_wspomagania_decyzji\dt\iriswithheader.data", ',', ".")
print(df)

# api.toNumeric(dt)
# api.toDiscrete(df,col="Przych",step=0.2)
# api.normalize(df,"Przych")
df = api.changeRange(df, "a", 0, 1)

df = api.changeRange(df, "c", 0, 1)
gui.plot2d(df, "a", "b")
gui.plot3d(df, "a", "b", "c")
gui.histogram(df,"a",-1)
