import requests
from bs4 import BeautifulSoup

def get_URL(url):
    links=[]
    counter=0
    website=requests.get(url).text
    soup=BeautifulSoup(website,'lxml')
    artical= soup.find('div', class_='mw-content-ltr')
    
    for link in artical.find_all('a'):
        links.append(link.get('href'))
        counter=counter+1
        if(link.text == 'Philosophy' or counter > 100 or len(links) == 0):
            break
        
    for link in links:
        print(link)
        
get_URL("https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy")

    