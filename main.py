from smspva_wrapper import Client, Backends, Services, Countries
from smspva_wrapper.types import country_dict, service_dict

SIMSMS_API_KEY = ''
SMSPVA_API_KEY = ''

c = Client(api_key=SMSPVA_API_KEY, backend=Backends.SMSPVA)


def cheapest_price_finder():
    prices = []
    for country in country_dict:
        a = c.get_service_price(Services.TELEGRAM, country)
        item = (a.price, a.country)
        prices.append(item)

    prices.sort()
    for item in prices:
        print(f"{item[1]}: {item[0]}")


if '__main__' == __name__:
    print(c.name)
    print(c.balance)
    print(c.karma)
    print(c.name)
    cheapest_price_finder()
