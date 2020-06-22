import requests
from bs4 import BeautifulSoup
import csv

#writing the data to a csv
file = csv.writer(open('artist.csv', 'w'))
file.writerow(['Name', 'Link'])


pages = []

for i in range(1, 5):
    url ='https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'lxml')

#removing the bottom list
last_links = soup.find(class_='AlphaNav')
last_links.decompose()


#pulling all the text
artist_name_list = soup.find(class_='BodyText')

artist_name_list_items = artist_name_list.find_all('a')


for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    #print(artist_name.prettify())
    print(names)
    print(links)

file.writerow([names, links])



    
