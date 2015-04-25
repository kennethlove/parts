import requests
from sys import argv
from bs4 import BeautifulSoup
import webbrowser

script, network, channel = argv


blacklist = ['feed', 'archive', 'newsletter']
class show(object):
    def __init__(self, network, channel):
        self.network  = network
        self.channel =  channel
        self.shows = []
        self.add_shows() 
    
    def add_shows(self):
        url = self.network + '/' + self.channel
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        #div = soup.find('div',{'class':'box'})
        #a = div.find_all('a')
        a = soup.find_all('a') #test
        
        for links in a:
            link_check = links['href']
            if link_check.startswith('/'+ self.channel) and not link_check.startswith('/' + self.channel + '/' + 'page') and link_check.split('/')[-1] != channel and link_check.split('/')[-1] not in blacklist:
                self.shows.append(self.network + links['href'])

    def get_shows(self):
        for a in self.shows:
            print(a)

tdb = show(network, channel)
tdb.get_shows()
