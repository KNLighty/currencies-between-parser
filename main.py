from urllib.request import urlopen
from xml.etree import ElementTree as etree

SOURCE = "http://www.cbr.ru/scripts/XML_daily.asp"
currency_to_id = {'HUF': 'R01135', 'NOK': 'R01535'}


def parse_currency_rate(currency):
    currency_id = currency_to_id[currency]
    request_string_value = './/Valute[@ID="%s"]/Value' % currency_id
    with urlopen(SOURCE, timeout=10) as r:
        currency_rate = etree.parse(r).findtext(request_string_value)
        currency_rate = currency_rate.replace(',', '.')
        return float(currency_rate) / parse_currency_nominal(currency)


def parse_currency_nominal(currency):
    currency_id = currency_to_id[currency]
    request_string_nominal = './/Valute[@ID="%s"]/Nominal' % currency_id
    with urlopen(SOURCE, timeout=10) as r:
        currency_nominal = etree.parse(r).findtext(request_string_nominal)
        return float(currency_nominal)


HUF_rate_rub = parse_currency_rate("HUF")
NOK_rate_rub = parse_currency_rate("NOK")

if __name__ == '__main__':
    print('Одна норвежская крона составляет', NOK_rate_rub / HUF_rate_rub, 'в венгерских форинтах')
