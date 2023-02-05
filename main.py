import csv
import os
import time

import requests
from bs4 import BeautifulSoup

_user_agent_header = {'User-Agent': 'wikipedia-tables-scraper'}


def scrap_page(url):
    response = requests.get(url, headers=_user_agent_header)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    rows = [table.find_all("tr") for table in tables]
    merged_rows = []
    for row in rows:
        merged_rows += row
    all_table_data = [row.find_all("td") for row in merged_rows]
    img_by_country = {data_for_row[0].text: data_for_row[1].find("img") for data_for_row in all_table_data if
                      len(data_for_row) == 3}
    img_src_by_country = {key: value["src"][2:] for key, value in img_by_country.items() if
                          value and value.has_attr("src")}
    return img_src_by_country


def write_img_to_csv_file(value_by_country, file_name):
    with open(f'../{file_name}', 'w', newline='') as file:
        writer = csv.writer(file)

        for key, value in value_by_country.items():
            file_name = get_file_name_from_url(value)
            writer.writerow([key, f'<img src=\'{file_name}\'>'])


def download_images(value_by_country, directory_name):
    if not os.path.exists(f'../{directory_name}'):
        os.makedirs(f'../{directory_name}')

    for _, url in value_by_country.items():
        retries_counter = 0

        while retries_counter < 3:
            retries_counter += 1
            response = requests.get(f'https://{url}', headers=_user_agent_header)
            if response.status_code != 200:
                print(f'Couldn\'t retrieve image from {url}. Waiting 3 seconds')
                time.sleep(3)
                continue
            write_response_to_file(directory_name, response, url)


def write_response_to_file(directory_name, response, url):
    file_name = get_file_name_from_url(url)
    with open(f'../{directory_name}/{file_name}', 'wb') as f:
        f.write(response.content)


def get_file_name_from_url(url):
    return url.split("/")[-1]


if __name__ == '__main__':
    img_url_by_country = scrap_page('https://pl.wikipedia.org/wiki/Herby_i_god%C5%82a_pa%C5%84stw_%C5%9Bwiata')
    write_img_to_csv_file(img_url_by_country, "herby.csv")
    download_images(img_url_by_country, "media")
