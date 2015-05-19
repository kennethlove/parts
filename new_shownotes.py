import requests
from bs4 import BeautifulSoup
from opml import *



class Network:
    def __init__(self, name):
        self.name = name[1]
        self.url = name[3]
        self.class_tag = name[2]
        self.show_list = {x:Podcast(x, self.get_url(x[1]), self.get_ep_list(self.get_url(x[1]), x[1])) for x in name[0]}
        
    def __str__(self):
        return(self.name)
    
    def get_url(self, podcast):
        return(self.url + podcast)
       
    def get_ep_list(self, show_url, show_name):
        bad_words = ['page']
        show_list = []
        web = requests.get(show_url)
        soup = BeautifulSoup(web.content)
        wrapper = soup.find("div", self.class_tag)
        for links in wrapper.findAll('a'):
            link = links['href']
            if link.startswith('/{}/'.format(show_name)):
                for word in bad_words:
                    if word not in link:
                        show_list.append(link)
        return(show_list)
        
class Podcast:
    def __init__(self, name, url, ep_list):
        self.name = name
        self.url = url
        self.ep_list = ep_list

filename = 'overcast.opml'
known_networks = {'5by5.tv':([],'5by5', 'box', 'http://5by5.tv'),
                      'relay.fm':([],'test'),
                      'rainmaker.fm':([],'test')
                      }
    
podcast_list = network_selection(get_opml(filename), known_networks)
fivebyfive = Network(podcast_list['5by5.tv'])
