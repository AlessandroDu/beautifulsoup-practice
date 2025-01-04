from bs4 import BeautifulSoup
import requests

# Learning The 20% of BeautifulSoup functions that will let me achieve 80% of scraping tasks

# 1. loading and parsing html
url = "https://google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 2. navigating the DOM
title = soup.find("h1") # First <h1>
links = soup.find_all("a", class_="example") # all <a> with class "example"

# 3. extracting text or attributes
text = title.text # get the text content
href = link["href"] # get the "href" attribute of a link

# 4. CSS selectors
links = soup.select("div.container a.example")

# 5. iterating over results
for link in links:
    print(link["href"])


"""
Building a Simple Web Scraper
    Example: Scraping Article Titles
    Objective: Scrape all article titles from a blog.
"""
url = "https://example-blog.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# find all article titles
articles = soup.find_all("h2", class_="article-title")

for article in articles:
    print(article.text)