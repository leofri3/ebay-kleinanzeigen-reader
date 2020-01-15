from urllib import request
from bs4 import BeautifulSoup
import re


#String with the html-code from the site
def get_html(searchWord):
    url_request = request.urlopen(
        "https://www.ebay-kleinanzeigen.de/s-" + searchWord + "/k0")

    if url_request.code == 200:
        html_content = str(url_request.read()).replace('\\n', '')

    return html_content

#List with touples wich contain the title and the price
def get_title_price(html_content):
    result = []
    soup = BeautifulSoup(html_content, 'html.parser')

    result_title_incomplete = soup.find_all(class_="ellipsis")
    result_price_incomplete = soup.find_all('strong')

    for i in range(0, len(result_title_incomplete)):
        title = re.findall('>.*?</a>', str(result_title_incomplete[i]))[0][1:-4]
        price = re.findall('>.*?<', str(result_price_incomplete[i]).replace(' \\xe2\\x82\\xac', ''))[0][1:-1]
        result.append((title, price))
    return result

print(get_title_price(get_html("oneplus")))