def get_opml(filename):
    opml = {}
    with open( filename,'r') as file:
        list_temp = (file.read().split('<outline')[1:])
        for line in list_temp:
            title_start = line.find('title=') + 7
            title_end = line.find('"',title_start)
            title = line[title_start:title_end]

            url_start = line.find('xmlUrl=') + 8
            url_end = line.find('"',url_start)       
            url = line[url_start:url_end]
            
            network = url.split('.')[1]
            opml[title.lower()] = url
        return(opml)    

def network_selection(opml,podcast_list):
    known_networks = {'5by5.tv':[] , 'relay.fm':[]}
    podcast_list = {}
    for url in opml:
        print(opml[url])
        for network in known_networks:
            print(network)
            if network in url:
                known_networks[network].append(url)
    return(known_networks)
print(network_selection(get_opml('overcast.opml'), {}))
## 
