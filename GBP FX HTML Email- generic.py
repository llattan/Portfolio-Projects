from urllib.request import urlopen
from bs4 import BeautifulSoup 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import time
import requests
import csv
#from email import encoders


url="https://finance.yahoo.com/quote/GBPUSD=X?p=GBPUSD=X&.tsrc=fin-srch"

def getFX(url):
		#returns a list of all news articles on BBC homepage
	html = urlopen(url)
	bsObj = BeautifulSoup(html, features = "html.parser")
	rate = bsObj.find("span", attrs={"class":'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'}).text
	print (rate)
	return rate
	
def get_url(symbol, years=1):
    # Builds a URL to access the CSV download file of a given ticker.  By default, returns one year of history.
    epoch_year = 31622400 # This is how many seconds are in a year, which is the basis of Epoch time.
    period2 = time.time()
    period1 = period2 - (years * epoch_year)
    url_formatted = ("https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%d&period2=%d&interval=1d&events=history" %
                     (symbol,
                      period1,
                      period2))
    return url_formatted

def get_file(symbol):
	url = get_url(symbol)
	with requests.Session() as s:
		download = s.get(url)
		decoded_content = download.content.decode('utf-8')
		cr = csv.reader(decoded_content.splitlines(), delimiter=',')		
		fileLines = list(cr)
		prevDays = []
		for i in range(-6,-1):
			prevDays.append(fileLines[i+1][0])
			prevDays.append(fileLines[i+1][4])
	return prevDays

cur_rate = getFX(url)
conv = "{:,}".format(round((1/float(cur_rate)*150000),2))
prevDays=get_file('GBPUSD=X')
print(prevDays)
for i in range(1, len(prevDays),2):
	prevDays[i] =  "{:,}".format(round((1/float(prevDays[i])*150000),2))

sender_email = "EMAIL SENDER"
receiver_email = "EMAIL RECEIVER"
password = "YOUR PASSWORD HERE"

message = MIMEMultipart("alternative")
message["Subject"] = "Daily GBP FX Conversion"
message["From"] = sender_email
message["To"] = receiver_email

html_file = open('/storage/emulated/0/Python/Portfolio/email html code.html')
html_body=html_file.read().replace("cur_rate", str(cur_rate)).replace("conv", str(conv)).replace("prevDays[0]", prevDays[0]).replace("prevDays[1]", prevDays[1]).replace("prevDays[2]", prevDays[2]).replace("prevDays[3]", prevDays[3]).replace("prevDays[4]", prevDays[4]).replace("prevDays[5]", prevDays[5]).replace("prevDays[6]", prevDays[6]).replace("prevDays[7]", prevDays[7]).replace("prevDays[8]", prevDays[8]).replace("prevDays[9]", prevDays[9])


# Create the plain-text and HTML version of your message
text = ("Good day!\n"+
		"\n"+
		" The GBP to USD FX rate is currently:" + str(cur_rate) +". At this price, \n\n" 
		"150k USD = " + str(conv)+ " GBP \n\n\n"+
		"The last 5 previous days were: \n"  + prevDays[0] + ": "+ prevDays[1] + " GBP\n"+ prevDays[2]+ ": " +prevDays[3] +" GBP\n"+prevDays[4]+ ": " +prevDays[5] +" GBP\n"+ prevDays[6]+ ": " +prevDays[7]+ " GBP\n"+	prevDays[8]+ ": " +prevDays[9] +" GBP\n"
		)


# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html_body, "html")
# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

message.attach(part1)
message.attach(part2)

#EMBED IMAGE FILES
banner_img = open('/storage/emulated/0/Python/Portfolio/notes-1158188.jpg', 'rb')
msgImage = MIMEImage(banner_img.read())
banner_img.close()

github_img = open('/storage/emulated/0/Python/Portfolio/Octocat.jpg', 'rb')
git_logoImage = MIMEImage(github_img.read())
github_img.close()

twitter_img = open('/storage/emulated/0/Python/Portfolio/Twitter_Logo_Blue.png', 'rb')
twitterImage = MIMEImage(twitter_img.read())
twitter_img.close()

LI_img = open('/storage/emulated/0/Python/Portfolio/LI-In-Bug.png', 'rb')
LinkedInImage = MIMEImage(LI_img.read())
LI_img.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<banner>')
git_logoImage.add_header('Content-ID', '<github>')
twitterImage.add_header('Content-ID', '<twitter>')
LinkedInImage.add_header('Content-ID', '<LI>')
message.attach(msgImage)
message.attach(git_logoImage)
message.attach(twitterImage)
message.attach(LinkedInImage)

#Attaching an image file to the email:
'''img_file = '/storage/emulated/0/Python/Portfolio/notes-1158188.jpg'
try:
	with open(img_file, 'rb') as attachment:
		part3 = MIMEBase("application","octet-stream")
		part3.set_payload(attachment.read())
	encoders.encode_base64(part3)
	part3.add_header("Content-Disposition",f"attachment; filename= {img_file}")
	message.attach(part3)
except Exception as e:
	print(f'Oh no! We didn\'t find the attachment! {e}')'''

# Create secure connection with server and send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )