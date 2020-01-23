class Offer:
    title = ''
    price = ''
    date = ''

    def __init__(self, title, price, date):
        self.title = str(title)
        self.price = str(price)
        self.date = str(date)

    def __str__(self):
        return self.title + ' ' + self.price + ' ' + self.date

