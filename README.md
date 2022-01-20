# assessment-for-pw

pip install requests 
pip install beautifulsoup4
pip install lxml

Python 3.10.0 

In the download.py the parent_dir must be pathed to before "/assessment-for-pw"

To get information about tax forms:
In terminal:
``` 
    python -c 'import main; print(main.taxFormInfo(form_terms_array))'
```

To download all the tax forms in a timeframe:
In terminal:
```
    python -c 'import download; download.download_links(search_term, first_year, last_year)'
```