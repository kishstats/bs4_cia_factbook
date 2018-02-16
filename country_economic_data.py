import requests
from bs4 import BeautifulSoup


def save_file(contents):
    with open('./files/testing.html', 'w') as f:
        f.write(contents)


def get_html_from_page(country_code='gm'):
    url = 'https://www.cia.gov/library/publications/the-world-factbook/geos/' \
        + country_code + '.html'

    response = requests.get(url)
    html = response.text
    return html


def get_html_from_file():
    with open('./files/testing.html', 'r') as f:
        return f.read()


def get_economic_list_item(_soup):
    parent_li = None
    div_tags = _soup.find_all(id='field')
    for div in div_tags:
        text = div.get_text()
        if 'purchasing power parity' in text:
            parent_li = div.find_parent('li')
    return parent_li


def get_economic_data(parent):
    economic_data = {}
    current_category = None

    div_tags = parent.find_all('div')
    for div in div_tags:
        if div.attrs.get('id') == 'field':
            current_category = div.get_text().replace(':', '').strip()
            economic_data[current_category] = []

        if div.get('class') and 'category_data' in div.get('class'):
            category_data = div.get_text()
            print('category_data: {}'.format(category_data))
            economic_data[current_category].append(category_data)

    return economic_data


def process_country_econ_data(country_code):
    html = get_html_from_page(country_code)
    soup = BeautifulSoup(html, 'html.parser')
    parent_li = get_economic_list_item(soup)

    return get_economic_data(parent_li)

if __name__ == "__main__":
    process_country_econ_data('gm')
