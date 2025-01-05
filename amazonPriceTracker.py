from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

url = "https://www.bol.com/nl/nl/ra/topdeals/386096"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')


prices = soup.find_all("span", class_="promo-price")
formatted_prices = []

for price in prices:
    # Extract the main part of the price (dollars)
    main_price = price.contents[0].strip()
    sup_element = price.find('sup')

    cents = ""

    if sup_element.text.replace(" ", "") != "-":
        cents = sup_element.get_text(strip=True)
    
    if cents:
        full_price = f"{main_price}.{cents}"
    else:
        full_price = main_price  # No cents
    
    # Remove commas (if present) and convert to a float
    formatted_price = float(full_price.replace(',', ''))
    formatted_prices.append(formatted_price)

print(formatted_prices)