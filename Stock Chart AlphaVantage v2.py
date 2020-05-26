import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
from datetime import datetime
import pandas_datareader.data as web
import matplotlib.dates as mdates

def create_plot(data, ticker):
	fig = plt.figure()
	fig.suptitle('20 Day Bollinger Band Analysis for ' + ticker)
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
	
	ax1.plot(x_vals,data['20Day_rolling_avg'], color='b', lw=2, label='20 Day SMA')
	ax1.plot(data['upper_Bollinger'], color='r', lw=1, label='Upper Band')
	ax1.plot(data['lower_Bollinger'], color='r', lw=1, label='Lower Band')
	ax1.plot(data['close'], label=' Daily Close Price')
	ax1.legend()
	
	ax2.plot(data['BandWidth'], color='g', label= 'Band Width')
	ax2.plot(data['20Day_STD'], label='20 Day Standard Dev')
	ax2.legend()
	
	#OPTION to fill in the area between the upper and lower Bollinger bands
	#x_axis = data.index.get_level_values(0)
	#ax1.fill_between(x_axis, data['upper_Bollinger'], data['lower_Bollinger'], color='grey')
	plt.show()

def getData(ticker):
	ticker = ticker
	func = 'av-daily'
	start = datetime(2019, 5, 1)
	end = datetime(2020, 5, 24)
	
	try:
		stk = web.DataReader(ticker, func, start,end, api_key='I00KMVP6LIGZB4MI')
		stk.index = pd.to_datetime(stk.index)
		stk['20Day_rolling_avg'] = stk['close'].rolling(window=20).mean()
		stk['long_rolling'] = stk['close'].rolling(window=200).mean()
		stk['20Day_STD'] = stk['close'].rolling(window=20).std()
		stk['upper_Bollinger'] = stk['20Day_rolling_avg'] + (stk['20Day_STD']*2)
		stk['lower_Bollinger'] = stk['20Day_rolling_avg'] - (stk['20Day_STD']*2)
		stk['BandWidth'] = ((stk['upper_Bollinger'] - stk['lower_Bollinger'])/stk['20Day_rolling_avg']*100)
		
		create_plot(stk, ticker)
	except Exception as e:
		print(e)

getData('AGG')



