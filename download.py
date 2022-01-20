# Import libraries
import requests
from bs4 import BeautifulSoup

def download_file(search_term, first_year, last_year):
    formatted_search_term = ""
    row_num = 0

    for char in search_term:
        if char == " ":
            char = "+"
        formatted_search_term += char

        results_asc = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?sortColumn=currentYearRevDate&indexOfFirstRow={row_num}&value={formatted_search_term}&criteria=formNumber&resultsPerPage=200&isDescending=false'

    req = requests.get(results_asc).text

    soup = BeautifulSoup(req, 'lxml')



    print(soup)

download_file("form w-2", 1991, 2022)

# with open(f'Downloads/{search_term}.txt', 'w') as f:
        #     f.write(str(d))

#try this one
# with open(f'{search_term}/{search_term}-{year}.pdf', 'wb') as f:
        #     f.write(str(d))


# downloadUrl = 'https://www.irs.gov/pub/irs-prior/fw2--1954.pdf'

# req = requests.get(downloadUrl)

# filename = req.url[downloadUrl.rfind('/')+1:]

# with open(filename, 'wb') as f:
#     for chunk in req.iter_content(chunk_size=8192):
#         if chunk:
#             f.write(chunk)