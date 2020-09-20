import requests
from bs4 import BeautifulSoup
import webbrowser


def get_data(url, file_name):

    page = requests.get(url)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, "html.parser")

    tbody = soup.find_all(id="myTable")

    f = open(file_name, "w+")
    records = []

    for elem in tbody:
        rows = elem.find_all("tr")
        for row in rows[1:301]:
            column = row.find("td")
            column_text = column.text[0] + column.text[1:].lower()
            records.append(column_text)

    for record in records:
        f.write(record + "\n")


url = "https://namecensus.com/data/1000.html"
file_name = "last_names.txt"
get_data(url, file_name)

url = "https://namecensus.com/male_names.htm"
file_name = "male_first_names.txt"
get_data(url, file_name)

url = "https://namecensus.com/female_names.htm"
file_name = "female_first_names.txt"
get_data(url, file_name)

