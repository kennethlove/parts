# Parts


Parts is a web scraping project that enables little hacks in my life using python. 

## Shownoter
Shownoter allows you to open all of the shownote links.

Shownoter utilizes the following tools:
 - [BeautifulSoup4][0]
 - [Requests][1]
 - [Webbrowser][2]
 
**How to Open**

Run Script followed by the network (Root URL) and the channel. (e.g. shownoter.py http://thisnetwork podcast)

**What does it do**

Shownoter will pull the latest episode from the channels and push the links directly to your browser. It pauses after 10 links. 

*You can can block certain sites using the **blacklist**.* You can add keywords or the entire url.

**Known Issues**

Only shows information from the latest episode. Working to create an interactive selection tool for shows


[0]:http://www.crummy.com/software/BeautifulSoup/ "Beautiful Soup"
[1]:http://docs.python-requests.org/en/latest/ "Requests"
[2]:http://pymotw.com/2/webbrowser/index.html "Web Browser"
