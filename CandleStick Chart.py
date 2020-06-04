import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas_datareader.data as web

def getData(ticker):
	ticker = ticker
	func = 'av-daily'
	start = datetime(2020, 5, 1)
	end = datetime(2020, 5, 24)
	
	try:
		stk = web.DataReader(ticker, func, start,end, api_key='I00KMVP6LIGZB4MI')
		stk.index = pd.to_datetime(stk.index)
		stk.sort_index()
		stk.rename(columns={'open': 'Open', 'close': 'Close', 'high': 'High', 'low': 'Low', 'volume':'Volume'}, inplace=True)
		print(stk)
		ax = mpf.plot(stk, type='candle', volume=True, style='starsandstripes', title="\n" +ticker +' Candle Stick Chart',
         ylabel='Price',
         ylabel_lower='Shares\nTraded')
	except Exception as e:
		print(e)

getData('AMZN')



