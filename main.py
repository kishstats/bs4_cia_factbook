import json
from country_list import get_countries
from country_economic_data import process_country_econ_data

get_countries()

countries = []
with open('./files/countries.txt', 'r') as f:
    countries = f.read().splitlines()

for country in countries[]:
    print("processing country: {}".format(country))
    econ_data = process_country_econ_data(country)

    with open('./files/countries/' + country + '.json', 'w') as f:
        f.write(json.dumps(econ_data))
