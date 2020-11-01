from django import template
from forex_python.converter import CurrencyRates

register = template.Library()


def convert(arg1, arg2, amount):
    try:
        c = CurrencyRates()
        value = round(amount * c.get_rate(arg1, arg2), 2)
        return value
    except:
        value = 0
        return value


register.filter('convert', convert)
