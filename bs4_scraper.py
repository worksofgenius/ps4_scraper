'''
Install required libraries in your terminal
pip install requests
pip install html5lib
pip install bs4
'''

# Import libraries
import requests
from bs4 import BeautifulSoup

# Specify target url
URL = "https://website.com/release/2/"

# # Select user agent: https://deviceatlas.com/blog/list-of-user-agent-strings
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
r = requests.get(url=URL, headers=headers)
# # print(r.content)

# # Parse html content
soup = BeautifulSoup(r.content, 'html5lib')
# # print(soup.prettify())

# # Choose your extractor:
# # Extract all urls in <a> tags
for link in soup.find_all('a'):
  print(link.get('href'))


# # Extract all urls in <a> tags with specific class
for link in soup.find_all('a', class_="whatever"):
  print(link.get('href'))


# # Extract all urls in <a> tags in a <div>
urls = []

for data in soup.findAll('div', class_="txt"):
    link = data.find('a')
    try:
      if 'href' in link.attrs:
        url = link.get('href')
        urls.append(url)
    except:
      pass
  
for url in urls:
  print(url)

# Bonus scenario
# Extracting with pagination
page = 1

urls = []

hasNextPage=True

while(hasNextPage):
  r = requests.get(f"https://website.com/release/{page}/").text
  soup = BeautifulSoup(r, 'lxml') 
  website = soup.find_all('div', class_="txt")
  for data in website:
    link = data.find('a')
    try:
      if 'href' in link.attrs:
        url = link.get('href')
        urls.append(url)
    except:
      pass
  
  for url in urls:
    print(url)
    
  print("-- Page ",page," --")

  if soup.find("li",class_='next') is None:
    hasNextPage=False

  page+=1
