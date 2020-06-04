#This web scraper obtains all news article links from the BBC homepage, randomly chooses a link, and then scrapes the title and introductory paragraph from the article. The link, title, and paragraph are printed to csv.

from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re
import random
import datetime
import csv

random.seed(datetime.datetime.now())
linkList =[]
homepage ="http://www.bbc.co.uk"	

def getLinks(url):
	#returns a list of all news articles on BBC homepage
	html = urlopen(url)
	bsObj = BeautifulSoup(html, features = "html.parser")
	links = bsObj.findAll('a', attrs={'href': re.compile("^(https://www.bbc.co.uk/news/).*[0-9]$")})
	for link in links:
		if link['href'][-1].isdigit() == False:
			continue
		if link not in linkList:
			linkList.append(link['href'])
	return linkList

def getContent(url):
	#returns a list of all news articles
	html = urlopen(url)
	bsObj = BeautifulSoup(html, features = "html.parser")
	blurb = bsObj.find("div", attrs={"class":"story-body__inner", "property":"articleBody"}).find("p", attrs={"class":"story-body__introduction"}).get_text()
	return blurb


def getTitle(url):
	#returns a list of all news articles
	html = urlopen(url)
	bsObj = BeautifulSoup(html, features = "html.parser")
	container = bsObj.find("div", attrs = {'class': 'story-body'})
	title= container.find("h1").get_text()
	title=title.upper()
	return title


	#Choose random link from scraped list of links
try:	
	getLinks(homepage)
	new_site = linkList[random.randint(0,len(linkList)-1)]
	print('Currently scraping: ' + new_site)
		#Write to CSV:
	with open('BBC_Articles.csv', 'w') as csv_file:
		field_names = ['URL', 'Title', 'Synopsis']
		writer = csv.DictWriter(csv_file, fieldnames = field_names)
		writer.writeheader()
		for i in range(0,4):
			writer.writerow({'URL': str(new_site),'Title': getTitle(new_site), 'Synopsis':getContent(new_site)})
			nextURLs = getLinks(new_site)
			new_site = nextURLs[random.randint(0,len(linkList)-1)]
			print('Next article: ' + new_site)
except:
	print("Error has occurred.")
	pass
	
print('-------------Script Completed Successfully------------------')


