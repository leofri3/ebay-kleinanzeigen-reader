class Offer:
    title = ''
    price = ''
    date = ''
    link = 'https://www.ebay-kleinanzeigen.de'

    def __init__(self, title, price, date, link):
        self.title = str(title)
        self.price = str(price)
        self.date = str(date)
        self.link += str(link)

    def __str__(self):
        return self.title + ' ' + self.price + ' ' + self.date + '' + self.link

