from bs4 import BeautifulSoup as BSHTML
import urllib

page = urllib.request.urlopen('https://github.com/abushoeb/emotag')
soup = BSHTML(page)
images = soup.findAll('img')

for image in images:
    #print image source
    print(image['src'])
    #print alternate text
    print(image['alt'])