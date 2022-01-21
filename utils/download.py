import os
import shutil
import requests
from bs4 import BeautifulSoup

# Helper function for download_links
def convert_links(download_links, form_name):

    # Creates a new folder to store links in
    directory = form_name
    parent_dir = os.getcwd()
    dirpath = os.path.join(parent_dir, directory)

    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        shutil.rmtree(dirpath)

    os.mkdir(dirpath)

    # Downloads each file to the folder
    for link in download_links:
        req = requests.get(link)
        year = link[-8:-4]
        filename = f"{form_name} - {year}.pdf"

        with open(f"{dirpath}/{filename}", 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


def download_links(search_term, first_year, last_year, row_num=0, all_doc_links=[]):
    formatted_search_term = ""
    correct_form_name = ''

    for char in search_term:
        if char == " ":
            char = "+"
        formatted_search_term += char

        results_asc = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?sortColumn=currentYearRevDate&indexOfFirstRow={row_num}&value={formatted_search_term}&criteria=formNumber&resultsPerPage=200&isDescending=false'

    req = requests.get(results_asc).text
    soup = BeautifulSoup(req, 'lxml')

    forms = soup.findAll('tr')
    for form in forms:
        form_name = form.find('td', class_='LeftCellSpacer')

        if not form_name:
            pass
        elif form_name:
            if form_name.text.lower().strip() == search_term.lower():
                correct_form_name = form_name.text.strip()
                doc_link = form_name.a['href']
                year = int(doc_link[-8:-4])

                if first_year <= year <= last_year:
                    all_doc_links.append(doc_link)
    
    # Recursively moves through pagination to satisfy conditions
    if year < first_year or year < last_year:
        row_num += 200
        return download_links(search_term, first_year, last_year, row_num, all_doc_links)

    convert_links(all_doc_links, correct_form_name)
