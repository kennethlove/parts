import requests
from sys import argv
from bs4 import BeautifulSoup
import webbrowser

script, network, channel = argv


blacklist = ['feed', 'archive', 'newsletter',channel,'mailto']
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
        a = soup.find_all('a')
        
        for links in a:
            if links['href'].startswith('/'+ self.channel) and not links['href'].startswith('/' + self.channel + '/' + 'page') and links['href'].split('/')[-1] != self.channel and links['href'].split('/')[-1] not in blacklist and links['href'].split('//')[-1] not in blacklist:    
                self.shows.append(self.network + links['href'])

    def get_shows(self):
        for a in self.shows:
            print(a)

podcast = show(network, channel)
#podcast.get_shows()

re =  requests.get(podcast.shows[0])
soup = BeautifulSoup(re.content)
links = soup.find_all('a')
for link in links:
    if not link['href'].startswith('/') and not link['href'].startswith('/' + channel + '/' + 'page') and link['href'].split('/')[-1] != channel and link['href'].split('/')[-1] not in blacklist and not link['href'].split(':')[0] in blacklist and not link['href'].startswith(network) and not network.split('.')[1] in link['href'].split('.'):
        print(link['href'])
