from sympy import *
# import qgrid
import matplotlib.pyplot as plt
# from pandasgui.datasets import titanic
import Gui as gui

import Api as api
import dataAcess as data
import traceback
import consoleapp as exec
df=None
while 1==1:
    try:
        df = exec.loop(df)


    except Exception:
        print(traceback.format_exc())
        print("error occured during code execution")
