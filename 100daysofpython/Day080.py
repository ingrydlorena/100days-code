'''
Day 80: Web scraping
Write a script to scrape data from a website.
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com/python/default.asp'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.find_all('h1')

    for heading in headings:
        print(heading.text.strip())
    
    links = soup.find_all('a', href=True)

    for link in links:
        print(link['href'])

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
