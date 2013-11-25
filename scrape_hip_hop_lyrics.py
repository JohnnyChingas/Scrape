from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
from unicodedata import normalize

BASE_URL = "http://ohhla.com/"

def get_links(section_url):
    links = []
    soup = get_soup(section_url)
    start = False
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        if tds[0].text.strip() == 'Last':
            start = True
        if start:
            for i in xrange(len(tds)):
                if i == 3:
                    try:    
                        links.append(BASE_URL+tds[i].find('a').get('href'))
                    except:
                        None
    return links

def get_lyrics(links):            
    for link in links:
        soup = get_soup(link)
        pres = soup.find_all('pre')
        if pres == []:
            text = clean_text(soup.text)
        else:
            text = clean_text(pres[0].text)
        sleep(1)

def get_soup(link):
    html = urlopen(link).read() 
    soup = BeautifulSoup(html, "lxml")
    return soup

def clean_text(text):
    text = text.replace('Artist','Tim')
    print '*'*100
    print text
    print '*'*100
    return text

if __name__ == '__main__':
    top_hip_hop = ("http://ohhla.com/most.html")

    links = get_links(top_hip_hop)
    get_lyrics(links)
