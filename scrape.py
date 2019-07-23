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
f= open("info.txt","w+")

## User name
user_name=page_soup.h1.text.strip()
print("Your User name:",user_name)
##City

city=page_soup.select('div.main-info a')
city_name=city[1].text.strip()
print("City:",city_name)
##Country
country_name=city[2].text.strip()
print("Country:",country_name)
##Institute or organisation name

organisation_name=city[3].text.strip()

## rank_name and rating and highest rating
rank=page_soup.select('div.info span')
rank_name=rank[0].text.strip()
print("You are:",rank_name)
rating=rank[1].text.strip()
print("Your rating is:",rating)
highest_rating=rank[4].text.strip()
print("Your highest rating is:",highest_rating)

##contribution

contribution=rank[5].text.strip()
print("Your Contribution:",contribution)
## Friends

Friends=page_soup.select('div.info li')
list_friends=Friends[2].text.strip()
print(list_friends)
## registered

registered=rank[7].text.strip()
print("You were Registered:",registered)
##last visit

last_visit=rank[6].text.strip()
print("Your last visit on CF:",last_visit)
f.close()