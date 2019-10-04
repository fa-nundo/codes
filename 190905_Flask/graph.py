from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import random
from flask import Flask, render_template, make_response


def plot_graph():
    from io import BytesIO
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


import stock
import pandas as pd
plot_data = pd.DataFrame(stock.get_csv('GOOG'))['High']
print(plot_data)

fig = Figure()
axis = fig.add_subplot(1, 1, 1)

xs = range(100)
ys = [random.randint(1, 50) for x in xs]
plot_data = pd.DataFrame(stock.get_csv('GOOG'))['High']
    
axis.plot(xs, ys)
