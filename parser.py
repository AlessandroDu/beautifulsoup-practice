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

# --------------------------------------

# advanced but essential features
# 1. pagination: scraping multiple pages
next_page = soup.find("a", class_="next-page")["href"]

# 2. handling dynamic content: use selenium if the site uses JS
# 3. saving data: save scraped data to a file or database
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])

    for article in articles:
        writer.writerow([article.text, article["href"]])

# 4. error handling: manage failed requests
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")

# ---------------------------------
# common challenges
# anti-scraping measures
# - CAPTCHAs: use services like 2Captcha if needed
# - Headers: spoof browser headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
# - proxies: rotate IP addresses with proxy services