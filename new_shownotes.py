import requests
from bs4 import BeautifulSoup

class Network:
    def __init__(self, name, url, class_tag, show_list):
        self.name = name
        self.url = url
        self.class_tag = class_tag
        self.show_list = {x:Podcast(x, self.get_url(x), self.get_ep_list(self.get_url(x), x)) for x in show_list}
        
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

fivebyfive = Network('5by5','http://5by5.tv/', 'box', ['dbh', 'b2w', 'supercharged'])      
for x in fivebyfive.show_list:
    print(fivebyfive.show_list[x].url)