class Network:
    def __init__(self, url, content):
        self.url = url
        self.content = content
    
    def get_podcast_url(self, podcast):
        return(self.url + podcast)

class Podcast:
    def __init__(self, url):
        self.url = url
    
fivebyfive = Network('http://5by5.tv/', 'content')
print(fivebyfive) 
