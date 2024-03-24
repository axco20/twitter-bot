import tweepy
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
import time
import random

authors = []
quotes = []
combined_list = []
n = 10

try:
   with open("C:\\Users\\xande\\OneDrive\\Desktop\\pyspace\\day_count.txt", 'r') as file:
      day = int(file.read())
except FileNotFoundError:
   print("error opening the file")

def scrape_website(page_number):
  page_num = str(page_number) 
  URL = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_num 
  webpage = requests.get(URL)  
  soup = BeautifulSoup(webpage.text, "html.parser")
  quoteText = soup.find_all('div', attrs={'class':'quoteText'}) 
  for i in quoteText:
    quote = i.text.strip().split('\n')[0]
    author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
    #print(quote)
    quotes.append(quote)
    #print(author)
    authors.append(author)

for num in range (0, n):
   scrape_website(num)

for i in range (len(quotes)):
   combined_list.append(quotes[i] + '-'+ authors[i])

random_quote = random.choice(combined_list)

client = tweepy.Client(consumer_key="jHqJyBhqkw1722jHXTFhN9azc",
consumer_secret="AT23aiy0vl9caj9VdRyovFYyaMKkPHL4zPlrEZ429HYxypP8o6",
access_token="1024867133199724544-2h9rv5itk3ZsJWjZkkQqZ1QSL99zUl",
access_token_secret="tEqmxvjHuIEGJw4WQV36HF5Ss3qrq8wujAzYtNeUUZuGw")

passedresponse = "GENERATED QUOTE OF THE DAY (DAY " + str(day) + "):\n" + random_quote
response = client.create_tweet(text=passedresponse)
print(response)

day += 1

try:
   with open("C:\\users\\xande\\OneDrive\\Desktop\\pyspace\\day_count.txt", 'w') as file:
      file.write(str(day))
except Exception as e:
   print("error writing to the file")