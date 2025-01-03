from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', 'lxml')
tag = soup.b

print (tag.attrs)