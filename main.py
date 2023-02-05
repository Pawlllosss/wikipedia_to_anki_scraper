import requests
from bs4 import BeautifulSoup


def scrap_page(url):
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    rows = [table.find_all("tr") for table in tables]
    merged_rows = []
    for row in rows:
        merged_rows += row
    all_table_data = [row.find_all("td") for row in merged_rows]
    img_by_country = {data_for_row[0].text: data_for_row[1].find("img") for data_for_row in all_table_data if
                      len(data_for_row) == 3}
    img_src_by_country = {key: value["src"][2:] for key, value in img_by_country.items() if value and value.has_attr("src")}
    return img_src_by_country


if __name__ == '__main__':
    img_url_by_country = scrap_page('https://pl.wikipedia.org/wiki/Herby_i_god%C5%82a_pa%C5%84stw_%C5%9Bwiata')
