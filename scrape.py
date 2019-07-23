import bs4
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

count=0
while(True):
	if(count==0):
		cf_id = input('Enter your codeforces user-id\n')
		count=count+1
	else:
		cf_id = input('Enter your codeforces user-id again\n')
	my_url='https://codeforces.com/profile/'+cf_id

	#INVALID-MSG
	message="Invalid user-id"
	#Check if id exits:
	check=requests.get(my_url,allow_redirects=True)
	if(check.url=='https://codeforces.com/'):
		print (message.center(40, '*'))  
	else:
		break


uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")


##Creating file
#f= open("info.txt","w+")

## User name
user_name=page_soup.h1.text.strip()
print("Your User name:",user_name)
##City

city=page_soup.select('div.main-info a')

try:
	data=city[1]
	print("Your City:",city[1].text.strip())
except IndexError:
	print("You City:______")

##Country
try:
	data=city[2]
	print("Country:",data.text.strip())
except IndexError:
	print("Country:_______")
##Institute or organisation name
try:
	data=city[3]
	print("Organisation:",data.text.strip())
except IndexError:
	print("Organisation:________")

## rank_name and rating and highest rating
rank=page_soup.select('div.info span')
try:
	rank_name=rank[0]
	print("You are:",rank_name.text.strip())
except IndexError:
	print("You are:No participation till now")

try:
	rating=rank[1]
	print("Your rating is:",rating.text.strip())
except IndexError:
	print("Your rating is:No participation till now")

try:
	highest_rating=rank[4]
	print("Your highest rating is:",highest_rating.text.strip())
except IndexError:
	print("You highest rating is:No participation till now")

##contribution

contribution=page_soup.select('li span')
print("Your Contribution:",contribution[0].text.strip())
## Friends

friend=page_soup.find_all('li')
list_friends=friend[41].text.strip()
print(list_friends)
## registered

registered=contribution[2].text.strip()
print("You were Registered:",registered)
##last visit

last_visit=contribution[1].text.strip()
print("Your last visit on CF:",last_visit)
#f.close()