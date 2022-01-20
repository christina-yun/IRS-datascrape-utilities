# assessment-for-pw

### Libraries to install
- pip install requests 
- pip install beautifulsoup4
- pip install lxml

### Python Version
Python 3.10.0 

### To get information about tax forms:

#### Format of 'form_terms_array'
- The form_terms_array argument is an array of strings
- Each string must be as written the way it's represented in 'Product Number' on IRS.gov website but can be upper or lower cased
    - Good: 'form 1040-ez', 'Form 1040-ez', 'Form 1040-EZ'
    - Bad: '1040-ez', '1040 ez', 'Form 1040 EZ'

#### CLI Command:
``` 
    python -c 'import main; print(main.taxFormInfo(form_terms_array))'
```
#### Input:
```
    taxFormInfo(["form w-2", "form 1040", "form 1095-a"])
```

#### Output:
```
[
    {
        "form_number": "Form W-2",
        "form_title": "Wage and Tax Statement (Info Copy Only)",
        "min_year": 1954,
        "max_year": 2022
    },
    {
        "form_number": "Form 1040",
        "form_title": "U.S. Individual Income Tax Return",
        "min_year": 1864,
        "max_year": 2021
    },
    {
        "form_number": "Form 1095-A",
        "form_title": "Health Insurance Marketplace Statement",
        "min_year": 2014,
        "max_year": 2021
    }
]
```

### To download tax forms in a given timeframe

#### Format of 'search_term', first_year, last_year
- The search_term string must be input as written for 'Product Number' on IRS.gov website but can be upper or lower cased
    - Good: 'form 1040-ez', 'Form 1040-ez', 'Form 1040-EZ'
    - Bad: '1040-ez', '1040 ez', 'Form 1040 EZ'
- The first_year and last_year terms are input as integers between 1864 and the current year inclusive.

#### CLI Command
```
    python -c 'import download; download.download_links(search_term, first_year, last_year)'
```

#### Input
```
    download_links("form 56", 1991, 1998)
```

#### Output
- A new directory in the project
    - /Form 56
    - 3 files with the naming convention 'Form 56 - {year}'
        - years: 1992, 1994, 1997
