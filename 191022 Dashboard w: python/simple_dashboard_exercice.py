__author__ = 'Florent'

import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from tkinter.ttk import *

df = pd.read_csv('https://nundo.fr/wp-content/uploads/2019/10/climbing_statistics.csv')

root = tk.Tk()
root.geometry("500x500")

combo = Combobox(root) 
combo['values']= tuple(i for i in df.columns.tolist())
combo.current(0) 
combo.pack(fill=tk.X)


def gets(m):
    height_val = df[m].value_counts().values
    bars_val = df[m].value_counts().index
    y_val = np.arange(len(bars_val))
    
    return(m, height_val, bars_val, y_val)
    
def plot():
    m = combo.get()
    
    m, height, bars, y = gets(m)
    
    lbl.configure(text= m)
    lbl.pack()
       
    fig = Figure(figsize=(12,12))
    a = fig.add_subplot(111)
    a.bar(y, height)

    print(y.mean())
    a.set_title ("Estimation Grid", fontsize=16)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)
        
    return(fig)
        
def plus():
    plot()
    canvas = FigureCanvasTkAgg(plot(), master=root)
    canvas.get_tk_widget().pack()
    canvas.draw()
    

button = Button(root, text="check", command=plus)
button.pack()

lbl = Label(root)
#canvas = FigureCanvasTkAgg(plot(), master=root)

#canvas = FigureCanvasTkAgg(plot(), master=root)
#canvas.get_tk_widget().pack()
#canvas.draw()

#start = mclass(root)



root.mainloop()