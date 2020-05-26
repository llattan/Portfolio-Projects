import requests
from bs4 import BeautifulSoup
import random
import csv
import os


def getFoodQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/food-trivia'
	for i in range(1, 11):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/food-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test
	
def getTechQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/computer-trivia/'
	for i in range(1, 5):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/computer-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test
	
def getAnimalQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/animal-trivia/'
	for i in range(1, 9):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/animal-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test

def getSciQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/science-trivia/'
	for i in range(1, 21):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/science-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test
	
def getMusicQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/music-trivia/'
	for i in range(1, 11):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/music-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test
	
def getGeoQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/geography-trivia/'
	for i in range(1, 21):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/geography-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test
	
def getHistQuestions():
	q_list =[]
	a_list =[]
	used_qs =[]
	start_url='https://trivia.fyi/category/history-trivia/'
	for i in range(1, 26):
		if i == 1:
			r = requests.get(start_url)
		else:
			url = ('https://trivia.fyi/category/history-trivia/page/%d' %i)
			r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("h2 >a")
		a = bsObj.find_all("div", "su-spoiler-content su-u-clearfix su-u-trim")
		
		for question in q:
			q_list.append(question.get_text())
	
		for answer in a:
			a_list.append(answer.get_text())
	#print(q_list)
	#print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test

def getRiddles():
	q_list =[]
	a_list =[]
	used_qs =[]
	for i in range(1,27):
		url = ('https://www.riddles.com/brain-teasers?page=%d' %i)
		r=requests.get(url)
		bsObj = BeautifulSoup(r.content, "html.parser")
		q = bsObj.select("blockquote p")
		a = bsObj.select("b > p")
	for question in q:
		q_list.append(question.get_text())
	
	for answer in a:
		a_list.append(answer.get_text())
	print(q_list)
	print(a_list)
	q_and_a = list(zip(q_list, a_list))
	
	dict={}
	for i in range(0,len(q_and_a)):
		dict[i]=q_and_a[i]
	test=[]
	for i in range(1, 10):
			rand = random.randint(0, len(dict)-1)
			while rand not in used_qs:
				test.append((dict[rand]))
				used_qs.append(rand)
			i-=1
	print(used_qs)
	#print(test)
	return test

def print_to_csv(content):
	subjects = ['Food', 'Technology', 'Nature', 'Science','Music', 'Geography', 'History']
	dir=os.getcwd()
	path = dir + '/Weekly_Lesbo_Trivia.csv'
	with open(path, 'w', newline='') as csvfile:
		quizwriter = csv.writer(csvfile, delimiter=',')
		quizwriter.writerow(['Question','Answer'])
		for func in content:
			quizwriter.writerow([subjects[content.index(func)]])	
			for row in func:
				quizwriter.writerow(row)
    

print(getRiddles())
#print(getHistQuestions())
#print(getMusicQuestions())
#print(getSciQuestions())
'''print_to_csv([getFoodQuestions(),
getTechQuestions(),getAnimalQuestions(), getSciQuestions(), getMusicQuestions(), getGeoQuestions(),getHistQuestions()])'''