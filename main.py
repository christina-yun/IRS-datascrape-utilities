from unicodedata import name
import requests
from bs4 import BeautifulSoup

def taxFormInfo(search_terms):
    formatted_search_info = []

    for search_term in search_terms:
        formatted_search_term = ""

        for char in search_term:
            if char == " ":
                char = "+"
            formatted_search_term += char

        results_asc = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?sortColumn=currentYearRevDate&indexOfFirstRow=0&value={formatted_search_term}&criteria=formNumber&resultsPerPage=200&isDescending=false'

        results_desc = f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?sortColumn=currentYearRevDate&indexOfFirstRow=0&value={formatted_search_term}&criteria=formNumber&resultsPerPage=200&isDescending=true'

        # Getting the first year
        html_text_asc = requests.get(results_asc).text
        soup_asc = BeautifulSoup(html_text_asc, 'lxml')

        first_form = soup_asc.find('tr', class_='even')
        form_number = first_form.find(
            'td', class_='LeftCellSpacer').text.strip()
        form_title = first_form.find(
            'td', class_='MiddleCellSpacer').text.strip()
        min_year = int(first_form.find('td', class_='EndCellSpacer').text.strip())

        # Getting the last year
        html_text_desc = requests.get(results_desc).text
        soup_desc = BeautifulSoup(html_text_desc, 'lxml')

        latest_year_correct_form = soup_desc.find_all(
            'td', class_='LeftCellSpacer')

        for correct_year in latest_year_correct_form:
            if correct_year.text.lower().strip() == search_term.lower().strip():
                max_year = int(correct_year.a['href'][-8:-4])
                break

        form_array_info = {
            'form_number': form_number,
            'form_title': form_title,
            'min_year': min_year,
            'max_year': max_year
        }

        formatted_search_info.append(form_array_info)

    return formatted_search_info
    