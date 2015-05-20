import requests
from bs4 import BeautifulSoup
from opml import *



class Network:
    def __init__(self, podcasts, name, class_tag, url):
        self.name = name
        self.class_tag = class_tag
        self.url = url
        self.show_list = {podcast[1]: Podcast(
            podcast,
            self.get_url(podcast[1]),
            self.get_ep_list(
                self.get_url(podcast[1]), podcast[1]
            )) for podcast in podcasts
        }
        
    def __str__(self):
        return self.name
    
    def get_url(self, podcast):
        return self.url + '/' + podcast
       
    def get_ep_list(self, show_url, show_name):
        bad_words = ['page']
        show_list = []
        web = requests.get(show_url)
        soup = BeautifulSoup(web.content)
        wrapper = soup.find("div", self.class_tag)
        for links in wrapper.findAll('a'):
            link = links['href']
            if link.startswith('/{}/'.format(show_name)) or link.startswith(self.url.rsplit('/',1)[0]):
                for word in bad_words:
                    if word not in link:
                        if link.startswith(self.url):
                            show_list.append(link)
                        else:
                            show_list.append(self.url + link)
        return show_list


class Podcast:
    def __init__(self, name, url, ep_list):
        self.name = name
        self.url = url
        self.ep_list = ep_list


filename = 'overcast.opml'
known_networks = {
    '5by5.tv':([], '5by5', 'box', 'http://5by5.tv'),
    'relay.fm':([], 'relay.fm', 'small-12 medium-8 columns episode__listing', 'http://relay.fm'),
    'rainmaker.fm':([], 'rainmaker.fm', 'content-sidebar-wrap', 'http://rainmaker.fm/series')
}

podcast_list = network_selection(get_opml(filename), known_networks)
for network in podcast_list:
    if network != 'misc':
        cast_network = Network(*podcast_list[network])
        for x in cast_network.show_list:
            print(cast_network.show_list[x].ep_list)
