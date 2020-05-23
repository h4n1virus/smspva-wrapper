from smspva_wrapper import Client, Services
from smspva_wrapper.types.countries import country_dict

SMSPVA_API_KEY = ''  # SIMSMS KEY

c = Client(api_key=SMSPVA_API_KEY, backend='smspva')  # backend is optional (defaults to smspva)

prices = []
for country in country_dict:
    a = c.get_service_price(service=Services.TELEGRAM, country=country)
    item = (a.price, a.country)
    prices.append(item)

prices.sort()

for item in prices:
    print(f"{item[1]}: {item[0]}")
