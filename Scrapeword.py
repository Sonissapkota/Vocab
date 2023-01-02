import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.vocabulary.com/lists/52473'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('li', class_="entry learnable")

wordlist = {}
for list in lists:
    word = list.find('a', class_="word").text
    meaning = list.find('div', class_="definition").text
    wordlist.update({word:meaning})

with open('word.JSON', 'w') as word_file:
     word_file.write(json.dumps(wordlist))
