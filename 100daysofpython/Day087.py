'''
Day 87: Web crawler
Create a web crawler or web scraper.
'''

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")


for quote in quotes:
    print(quote.get_text)