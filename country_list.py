import os
import requests
from bs4 import BeautifulSoup


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def country_code_for_href(href):
    idx_html = href.index('.html')
    return href[idx_html-2:idx_html]


def get_countries():
    create_dir_if_not_exists('files/countries')

    url = 'https://www.cia.gov/library/publications/the-world-factbook/rankorder/2004rank.html'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find(id='rankOrder')

    country_codes = []

    rows = table.find_all('tr')
    for row in rows:
        target_column = row.find_all('td', 'region')
        if target_column:
            link = target_column[0].find('a')
            href = link['href']
            country_code = country_code_for_href(href)
            print('country_code: {}'.format(country_code))
            country_codes.append(country_code)

    with open('./files/countries.txt', 'a') as f:
        for country_code in country_codes:
            f.write(country_code + '\n')

if __name__ == "__main__":
    get_countries()
