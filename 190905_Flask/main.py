from flask import Flask, render_template, make_response
app = Flask(__name__)
# Import files
import stock
#import graph
# Import librairies
import pandas as pd
import datetime as dt
from pandas_datareader import data
import pandas_datareader as pdr
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import random

@app.route("/")
def hello():
    stocks = stock.get_csv_html('GOOG')
    return render_template("accueil.html", google_stocks=stocks)

@app.route('/images/plot.png')
def plotrr():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    plot_data = pd.DataFrame(stock.get_csv('GOOG'))['High']
    
    axis.plot(plot_data)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/images/plot_bitcoin.png')
def plot_btc():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    plot_btc = stock.get_csv_scrap_btc()
    date = plot_btc['Date']
    data = plot_btc['High']
    
    axis.plot(date, data)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/images/plot_gold.png')
def plot_gold():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    gold_stocks = stock.get_csv_gold()
    gold_stocks_2017 = gold_stocks[gold_stocks['Date'] > '2016-12-01']
    date = gold_stocks_2017['Date']
    data = gold_stocks_2017['Price']
    
    axis.plot(date, data)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/images/plot_realestate.png')
def plot_realestate():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    realestate_stocks = stock.get_html_realestate()
    date = realestate_stocks['Date']
    data = realestate_stocks['High']
    
    axis.plot(date, data)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/images/plot_nasdaq100.png')
def plot_ndx():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    plot_data = pd.DataFrame(stock.get_csv('NDX'))['High']
    
    axis.plot(plot_data)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route("/to")
def get_to():
    return pd.read_csv('data/export.csv').to_html()


if __name__ == "__main__":
    app.run()