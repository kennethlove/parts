class Network:
    def __init__(self, name, podcasts, url='need to get', div='need to get'):
        self.name = name
        self.url = url
        self.div = div
        self.show_list = {podcast[0]: Podcast(podcast[1], podcast[1]) for podcast in podcasts}

    def __str__(self):
        return('{}: {}'.format(self.name, self.show_list))


class Podcast:
    def __init__(self, name, url, div='need to get'):
        self.name = name
        self.url = url
        self.div = div
        self.ep_list = ['some data here']

    def __str__(self):
       return '{}: {}'.format(self.name, self.ep_list)

    def get_ep_list(self):
        pass


#defines parameters to pull from opml file. Used in get_opml
def get_markers(line, tag, end_tag):  
    start = line.find(tag) + (len(tag) + 1)
    end = line.find('"', start)
    return line[start:end]


#reads the opml file and generates the Network and Podcast Objects
def get_opml(filename):
    with open(filename, 'r') as file:
        list_temp = (file.read().split('<outline')[1:]) #skips first value as it is xml data
        shows = {}
        for line in list_temp:
            title = get_markers(line, 'title=', '"')
            xml = get_markers(line, 'xmlUrl=', '"')
            html = get_markers(line, 'htmlUrl=', '"')
            xmlval = xml.split('/', 3)[2:]

            if xmlval[0] not in shows:
                shows[xmlval[0]] = shows.get(xmlval[0], [(title,xmlval[1])])
            else:
                shows[xmlval[0]].append((title, xmlval[1]))
        for item in shows:
            if len(shows[item]) == 1:
                shows[item] = Podcast(shows[item][0][0], item)
            else:
                shows[item] = Network(item, shows[item]) 
        return shows


filename = 'overcast.opml'
shows = get_opml(filename)
print(shows['feeds.5by5.tv'].show_list['On the Grid'])
