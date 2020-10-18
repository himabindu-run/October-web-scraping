from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import io

# Python code to illustrate append() mode 
f = open('results.csv','w') 
f.write("Title,Views\n") 
f.close() 

url_query = "https://www.youtube.com/results?search_query="
#query = (input("What do you want to search?")).replace(" ","+")
query = "hello world".replace(" ","+")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url_query+query)

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")

results = soup.findAll('a',href=True, attrs={'id':'video-title'})

# print(results[0].find('yt-formatted-string').get_text())
# print(results[0].get('aria-label'))

for result in results:
    print(result.find('yt-formatted-string').get_text(), end="\t")
    temp = result.get('aria-label').split(' ')
    print(temp[-2])


with io.open("results.csv", "a", encoding="utf-8") as f: 
    for result in results:
        temp = result.get('aria-label').split(' ')
        f.write( result.find('yt-formatted-string').get_text() + "," + temp[-2].replace(",",".") +"\n")


