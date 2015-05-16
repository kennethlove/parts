import requests
from bs4 import BeautifulSoup as soup

networks = {}
networks['5by5'] = {
    'url':'http://5by5.tv/',
    'content_header':'<content_sub1>'
    }
    
class show:
    def __init__(self,name,network,code = ''):
        self.name = name
        self.network = network
        self.code = self.get_code(code)
        self.url = networks[network]['url'] + self.code
    
    def get_code(self,code):
        if not code:
            return(self.name)
        else:
            return(code)

supercharged = show('supercharged','5by5')
print(supercharged.url)

