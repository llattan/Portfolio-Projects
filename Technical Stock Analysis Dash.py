import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
import mpl_finance as mpf
from matplotlib.gridspec import GridSpec
from datetime import datetime
import pandas_datareader.data as web
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

fig = plt.figure()
gs = GridSpec(ncols=4, nrows=4, hspace =.25)

ax1 = fig.add_subplot(gs[0:2,0:2])
ax2 = fig.add_subplot(gs[2,0:2])
ax3 = fig.add_subplot(gs[3,:])
ax4 = fig.add_subplot(gs[0:2,2:4])
ax5 = fig.add_subplot(gs[2,2:4])
ax=plt.gca()
		#gca method - Get the current figure's' Axes instance on the current figure matching the given keyword args, or create one.

def create_MACDplot(data, ticker):
	#Fix x-axis to monthly freq
	x_vals=data.index
	
	formatter = mdates.DateFormatter("%Y-%m")
	ax.xaxis.set_major_formatter(formatter)
	locator = mdates.MonthLocator()
	ax.xaxis.set_major_locator(locator)
	ax.xaxis.set_minor_locator(mdates.MonthLocator())
	font={'weight':'normal',
				'size':12}
	ax3.set_title('MACD and Signal Line Plot', fontdict=font)	

	ax3.plot(x_vals, data['MACD'], label='MACD')
	ax3.plot(x_vals, data['SignalLine'], label='Signal Line')
	ax3.bar(x_vals, data['MACD Hist'])
	ax3.set_ylabel('Price (USD)')
	ax3.set_xlabel('Date')
	ax3.legend()

def create_Bollplot(data, ticker):
	x_vals=data.index
	formatter = mdates.DateFormatter("%Y-%m")
	ax.xaxis.set_major_formatter(formatter)
	locator = mdates.MonthLocator()
	ax.xaxis.set_major_locator(locator)
	ax1.plot(x_vals,data['20Day_SMA'], color='b', lw=2, label='20 Day SMA')
	ax1.plot(data['upper_Bollinger'], color='r', lw=1, label='Upper Band')
	ax1.plot(data['lower_Bollinger'], color='r', lw=1, label='Lower Band')
	ax1.plot(data['close'], label=' Daily Close Price')
	font={'weight':'normal',
				'size':12}
	ax1.set_title('Bollinger Bands Analysis: ' + ticker, fontdict=font)
	ax1.legend()
	
	ax2.plot(data['BandWidth'], color='g', label= 'Band Width')
	ax2.plot(data['20Day_STD'], label='20 Day Standard Dev')
	ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
	ax2_locator = mdates.MonthLocator()
	ax2.xaxis.set_major_locator(ax2_locator)
	
	ax2.set_title('Band Width and Standard Dev', fontdict=font)
	ax2.legend()

def create_EMAplot(data, ticker):
	formatter = mdates.DateFormatter("%Y-%m")
	ax.xaxis.set_major_formatter(formatter)
	locator = mdates.YearLocator()
	ax.xaxis.set_major_locator(locator)
	#ax.xaxis.set_minor_locator(mdates.MonthLocator())
	font={'weight':'normal',
				'size':12}
	ax4.set_title('Candlestick', fontdict=font)
	#To make the chart more readable, get one month of data
	x_vals=data.index
	mpf.candlestick2_ochl(ax4,  data["open"], data["close"],data["high"], data["low"], width=.5, colorup='k', colordown='r', alpha=0.75)
	ax.xaxis.set_major_formatter(formatter)
	ax4.set_ylabel('Price (USD)')
	ax4.legend()
	
	ax5.bar(x_vals, data['volume'])
	ax5.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
	ax5_locator = mdates.MonthLocator()
	ax5.xaxis.set_major_locator(ax5_locator)
	ax5.set_ylabel('Price (USD)')
	ax5.set_xlabel('Date')
	font={'weight':'normal',
				'size':12}
	ax5.set_title("Volume (x10,000,000)", fontdict=font)
	ax5.legend()


def getData(ticker):
	ticker = ticker
	func = 'av-daily'
	start = datetime(2020, 1, 1)
	end = datetime(2020, 5, 24)
	main_font={'weight':'bold',
				'size':18}
	fig.suptitle('Technical Analysis for ' + ticker, fontdict = main_font)
	try:
		stk = web.DataReader(ticker, func, start,end, api_key='I00KMVP6LIGZB4MI')
		stk.index = pd.to_datetime(stk.index)
		stk.sort_index()
		stk['20Day_SMA'] = stk['close'].rolling(window=20).mean()
		stk['long_rolling'] = stk['close'].rolling(window=200).mean()
		stk['20Day_STD'] = stk['close'].rolling(window=20).std()
		stk['upper_Bollinger'] = stk['20Day_SMA'] + (stk['20Day_STD']*2)
		stk['lower_Bollinger'] = stk['20Day_SMA'] - (stk['20Day_STD']*2)
		stk['BandWidth'] = ((stk['upper_Bollinger'] - stk['lower_Bollinger'])/stk['20Day_SMA']*100)
		stk['EMA'] = stk['close'].ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()
		#MACD = (12D EMA - 26D EMA)
		stk['MACD'] = (stk['close'].ewm(span=12,min_periods=0,adjust=False,ignore_na=False).mean()) -(stk['close'].ewm(span=26,min_periods=0,adjust=False,ignore_na=False).mean())
		#signal Line = 9 day EMA of MACD
		stk['SignalLine'] = stk['MACD'].ewm(span=9,min_periods=0,adjust=False,ignore_na=False).mean()
		#MACD Histogram = MACD - Signal Line
		stk['MACD Hist'] = stk['MACD'] - stk['SignalLine']
		#print(stk)
		create_Bollplot(stk, ticker)
		create_MACDplot(stk, ticker)
		create_EMAplot(stk, ticker)
		plt.show()
	except Exception as e:
		print(e)

getData('AMZN')



