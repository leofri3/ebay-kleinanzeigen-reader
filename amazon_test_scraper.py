from urllib import request
from bs4 import BeautifulSoup
from datetime import date, timedelta
import offer


parameters = ['lowest_price', 'highest_price', 'oldest_date', 'newest_date']
result = []


# Prepare search word for url
def check_search_word(search_word):
    search_word = str(search_word).replace(' ', '-')
    return search_word


# String with the html-code from the site
def get_html(search_word, site):
    search_word = check_search_word(search_word)
    url_string = "https://www.ebay-kleinanzeigen.de/s-seite:" + str(site) + "/" + search_word + "/k0"
    url_request = request.urlopen(url_string)
    print(str(url_string))
    if url_request.code == 200:
        html_content = str(url_request.read()).replace('\\n', '')

    return html_content


def check_date(date_to_check):
    if 'Heute,' in date_to_check:
        return date.today().__format__('%d.%m.%Y')
    if 'Gestern,' in date_to_check:
        return date.strftime(date.today() - timedelta(1), '%d.%m.%Y')
    else:
        return date_to_check


# List with tuples which contain the title and the price
def get_title_and_price(html_content):
    result = []
    soup = BeautifulSoup(html_content, 'html.parser')

    result_title_incomplete = soup.find_all(class_="ellipsis")
    result_price_incomplete = soup.find_all('strong')
    result_date_incomplete = soup.find_all(class_="aditem-addon")

    for i in range(0, len(result_title_incomplete)):
        title = str(result_title_incomplete[i].getText())
        price = str(result_price_incomplete[i].getText()).replace(' \\xe2\\x82\\xac', '')
        date = str(result_date_incomplete[i].getText()).replace('                    ', '')
        link = str(result_title_incomplete[i].get('href'))
        date = check_date(date)
        result.append(offer.Offer(title, price, date, link))
    return result


def search_more_sites(number_sites, search_word):
    result = []
    for i in range(0, number_sites):
        result += get_title_and_price(get_html(search_word, i + 1))

    return result


def sort_list(content, parameter):
    if parameter == 'oldest_date':
        return sorted(content, key=lambda x: x.date)
    elif parameter == 'newest_date':
        return sorted(content, reverse=True, key=lambda x: x.date)
    elif parameter == 'lowest_price':
        return sorted(content, key=lambda x: x.price)
    elif parameter == 'highest_price':
        return sorted(content, reverse=True, key=lambda x: x.price)


# Outputs the List with results
def output(content):
    for entry in content:
        print('title: ' + entry.title + ' price:' + entry.price + ' date: ' + entry.date + ' link: ' + entry.link)


result = search_more_sites(10, 'oneplus 6t')
output(result)
