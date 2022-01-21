# assessment-for-pw

### Other notes and feedback
- This might be strange to say but I had a lot of fun putting this project together. I really enjoyed organizing everything and seeing the utilities working correctly. Doing it made me all the more excited to be considered at Pinwheel!

- Thank you for making this open-ended in terms of timing. I feel like I did much better work by not having it timed.

- The only piece of feedback I have about the challenge itself would be that it would've been really nice to have a picture/example of the file structure for the second utility (downloading the tax forms). It took me awhile to realize that I needed the separate folder to also be named after the IRS form number.

### Libraries to install
- pip install requests 
- pip install beautifulsoup4
- pip install lxml

### Python Version
Python 3.10.0 

### To get information about tax forms:
- You will need to run a CLI command (as noted and exampled below)
- It will return an array of JSON objects each with the form_number, form_title, min_year, and max_year in the command line.

#### Format of 'form_terms_array'
- The form_terms_array argument is an array of strings
- Each string must be as written the way it's represented in 'Product Number' on IRS.gov website but can be upper or lower cased
    - Good: 'form 1040-ez', 'Form 1040-ez', 'Form 1040-EZ'
    - Bad: '1040-ez', '1040 ez', 'Form 1040 EZ'
```
    array [ string, string, string, etc.]
```

#### CLI Command Format:
``` 
    python -c 'from utils import main; print(main.taxFormInfo(form_terms_array))'
```
#### Input Example:
```
    python -c 'from utils import main; print(main.taxFormInfo(["form w-2", "form 1040", "form 1095-a"]))'
```

#### Output Example:
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
- You will need to run a CLI command (as noted and exampled below)
- All files will be downloaded to a folder on the same level as the utils folder

#### Format of 'search_term', first_year, last_year
- The first_year and last_year terms are input as integers between 1864 and the current year inclusive.
- first_year <= last_year
- The search_term string must be input as written for 'Product Number' on IRS.gov website but can be upper or lower cased
    - Good: 'form 1040-ez', 'Form 1040-ez', 'Form 1040-EZ'
    - Bad: '1040-ez', '1040 ez', 'Form 1040 EZ'
```
    search_term = string
    first_year = 1864 <= int <= current year (2022)
    last_year = first_year <= int <= current year (2022)
```

#### CLI Command Format
```
    python -c 'from utils import download; download.download_links(search_term, first_year, last_year)'
```

#### Input example
```
    python -c 'from utils import download; download.download_links("form 56", 1991, 1998)'
```

#### Output example
- A new directory in the project
    - /Form 56
    - 3 pdf files with the naming convention 'Form 56 - {year}'
        - years: 1992, 1994, 1997
