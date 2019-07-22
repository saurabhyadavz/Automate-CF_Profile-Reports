import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

cf_id = input('Enter your codeforces user-id\n')

my_url='https://codeforces.com/profile/'+cf_id

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")


##Creating file
f= open("info.txt","w+")

## User name
user_name=page_soup.h1.text.strip()
print("Your User name is",user_name)
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
rank_name=rank[0]
print("You are:",rank_name)
rating=rank[1]
print("Your rating is:",rating)
highest_rating=rank[4].text.strip()
print("Your highest rating is:",hightest_rating)
##rating color

rating_color=rank[3].text.strip()
print("Your rating:",rating_color)
##contribution

contribution=rank[5].text.strip()

## Friends

Friends=page_soup.select('div.info li')
list_friends=Friends[2].text.strip()

## registered

registered=rank[7].text.strip()

##last visit

last_visit=rank[6].text.strip()

f.close()