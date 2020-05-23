from smspva_wrapper import Client, Services


SIMSMS_API_KEY = 'cqbeEXDLIGbRa1bUgs3Rkhk0dtE4Nh'  # SIMSMS KEY

c = Client(api_key=SIMSMS_API_KEY, backend='smspva')

"""
c = Client(api_key=SIMSMS_API_KEY, backend='smspva')

prices = []
for country in country_dict:
    a = c.get_service_price(service=Services.TELEGRAM, country=country)
    item = (a.price, a.country)
    prices.append(item)

prices.sort()

for item in prices:
    print(f"{item[1]}: {item[0]}")
"""