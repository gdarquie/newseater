from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime

driver = webdriver.Chrome("/Users/gaetan/devtool/chromedriver")

titles = []
paragraphs = []

now = datetime.datetime.now()
date_time = now.strftime("%m%d%Y_%H%M%S")

# Le Monde
driver.get("https://www.lemonde.fr/")

content = driver.page_source
soup = BeautifulSoup(content)

for h1 in soup.findAll('h1', {'class': 'article__title'}):
    titles.append(h1.text)

for p in soup.findAll('p', {'class': 'article__title'}):
    titles.append(p.text)

df = pd.DataFrame({'Titres': titles})  # add the writers of the articles
file_name = date_time + 'lemonde.csv'
df.to_csv('lemonde/' + file_name, index=False, encoding='utf-8')

# Le Figaro
driver.get("https://www.lefigaro.fr/")

titles = []
paragraphs = []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a', {'class': 'css-1dtv9cv esdb6og6'}):
    titles.append(a.text)

df = pd.DataFrame({'Titres': titles})  # add the writers of the articles
file_name = date_time + 'figaro.csv'
df.to_csv('figaro/' + file_name, index=False, encoding='utf-8')

# Libération

driver.get("https://www.liberation.fr/")

titles = []
paragraphs = []
content = driver.page_source
soup = BeautifulSoup(content)

for h2 in soup.findAll('h2'):
    titles.append(h2.text)

for h3 in soup.findAll('h3', {'class': 'live-title'}):
    titles.append(h3.text)

df = pd.DataFrame({'Titres': titles})  # add the writers of the articles
file_name = date_time + 'liberation.csv'
df.to_csv('liberation/' + file_name, index=False, encoding='utf-8')

driver.close()
