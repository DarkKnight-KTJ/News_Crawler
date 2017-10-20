import bs4 as bs
import urllib.request
source=urllib.request.urlopen('https://www.ndtv.com/top-stories').read()

soup=bs.BeautifulSoup(source,"html.parser")
print(" "*20,"TOP STORIES - NDTV")
print("")

print('*'*80)

for div in soup.findAll('div', {'class':'new_storylising_contentwrap'}):
    for url in div.findAll('a'):
        print(url.text.strip())
        print("")
        break
        
    for content in div.findAll('div', class_='nstory_intro'):
        print("     ",content.text.strip())
        print("")
        
        
    print('*'*80)
    print("")
    
    
                        
    
    
