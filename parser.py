from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', 'lxml')
tag = soup.html
tag.name = "strong"
print (tag)