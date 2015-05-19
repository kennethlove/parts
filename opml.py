def get_markers(line, tag, end_tag):
    start = line.find(tag) + (len(tag) + 1)
    end = line.find('"',start)
    return(line[start:end])
    

def get_opml(filename):
    opml = {}
    with open( filename,'r') as file:
        list_temp = (file.read().split('<outline')[1:])
        for line in list_temp:
            title = get_markers(line, 'title=', '"')   
            url = get_markers(line,'xmlUrl=','"')
            network = url.split('.')[1]
            opml[title.lower()] = url
        return(opml)    

def network_selection(opml, known_networks):
    known_networks['misc'] = []
    for url in opml:
        for network in known_networks:
            bad_words = ['','feed']
            i = 1
            while opml[url].split('/')[-i] in bad_words:
                i += 1
            if network in opml[url]:
                known_networks[network][0].append((url, opml[url].split('/')[-i]))
            else:
                known_networks['misc'].append((url, opml[url]))
    return(known_networks)
##filename = 'overcast.opml'
##known_networks = {'5by5.tv':[],
##                      'relay.fm':[],
##                      'rainmaker.fm':[],
##                      }
##networks = network_selection(get_opml(filename), known_networks)
##for x in networks:
##    if x != 'misc':
##        print(x, networks[x])
    
