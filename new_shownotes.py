import requests
from bs4 import BeautifulSoup as soup

networks = {}
networks['5by5'] = {
    'url':'http://5by5.tv',
    'content_header':'<content_sub1>'
    }
    
class show:
    def __init__(self,name,network,code = '/'):
        self.name = name
        self.network = network
        self.code = self.get_code(code)
        self.url = networks[network]['url'] + self.code
        self.episodes = self.get_episodes(self.url, self.code)    

    def get_code(self,code):
        if code == '/':
            return(code + self.name)
        elif not code.startswith('/'):
            return('/' + code)
        else:
            return(code)

    def get_episodes(self, url, code):
        r = requests.get(url)
        bs = soup(r.content)
        hrefs = bs.findAll('a')
        return([link['href'] for link in hrefs if link['href'].startswith(code) or link['href'].startswith(url)])
            
        return(bs)

dbh = show('dbh','5by5')
print(dbh.episodes)    

