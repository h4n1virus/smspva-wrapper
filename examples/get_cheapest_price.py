from smspva_wrapper import Client, Services
from smspva_wrapper.types import country_dict

SIMSMS_API_KEY = ''  # SIMSMS KEY

c = Client(api_key=SIMSMS_API_KEY)


prices = []
for country in country_dict:
    a = c.get_service_price(Services.TELEGRAM, country)
    item = (a.price, a.country)
    prices.append(item)

prices.sort()

for item in prices:
    print(f"{item[1]}: {item[0]}")
