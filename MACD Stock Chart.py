import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from datetime import datetime
import pandas_datareader.data as web
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


def create_plot(data, ticker):
	fig = plt.figure()
	#fig.suptitle('Technical Analysis for ' + ticker)
	gs = GridSpec(2, 1, hspace =0, height_ratios=[5,1])
	
	ax1 = fig.add_subplot(gs[0])
	ax2 = fig.add_subplot(gs[1])
	#Fix x-axis to monthly freq
	x_vals=data.index
		#gca method - Get the current figure's' Axes instance on the current figure matching the given keyword args, or create one.
	ax=plt.gca()
	formatter = mdates.DateFormatter("%Y-%m")
	ax.xaxis.set_major_formatter(formatter)
	locator = mdates.MonthLocator()
	ax.xaxis.set_major_locator(locator)
	ax.xaxis.set_minor_locator(mdates.MonthLocator())
	font={'weight':'bold',
				'size':18}
	ax1.set_title('Exponential Moving Average and MACD for ' + ticker, fontdict=font)
	
	
	ax1.plot(x_vals, data['EMA'], color='b', lw=2, label='20 Day EMA')
	ax1.plot(x_vals, data['close'], color='red', lw=1, label='Daily Close Price')
	ax1.set_ylabel('Price (USD)')
	ax1.legend()

	
	ax2.plot(x_vals, data['MACD'], label='MACD')
	ax2.plot(x_vals, data['SignalLine'], label='Signal Line')
	ax2.bar(x_vals, data['MACD Hist'])
	ax2.set_ylabel('Price (USD)')
	ax2.set_xlabel('Date')
	ax2.legend()
	plt.show()

def getData(ticker):
	ticker = ticker
	func = 'av-daily'
	start = datetime(2020, 1, 1)
	end = datetime(2020, 5, 24)
	
	try:
		stk = web.DataReader(ticker, func, start,end, api_key='I00KMVP6LIGZB4MI')
		stk.index = pd.to_datetime(stk.index)
		stk.sort_index()
		stk['20Day_SMA'] = stk['close'].rolling(window=20).mean()
		stk['EMA'] = stk['close'].ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()
		#MACD = (12D EMA - 26D EMA)
		stk['MACD'] = (stk['close'].ewm(span=12,min_periods=0,adjust=False,ignore_na=False).mean()) -(stk['close'].ewm(span=26,min_periods=0,adjust=False,ignore_na=False).mean())
		#signal Line = 9 day EMA of MACD
		stk['SignalLine'] = stk['MACD'].ewm(span=9,min_periods=0,adjust=False,ignore_na=False).mean()
		#MACD Histogram = MACD - Signal Line
		stk['MACD Hist'] = stk['MACD'] - stk['SignalLine']
		#print(stk)
		create_plot(stk, ticker)
	except Exception as e:
		print(e)

getData('AMZN')



