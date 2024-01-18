A python script to webscrape the wikipedia page containing a list of [Irish towns](https://en.wikipedia.org/wiki/List_of_towns_and_villages_in_the_Republic_of_Ireland), their coordinates and the provinces they belong to. 

It generates a JSON file with the following structure

```
[
  {
    "city": "Abbeydorney",
    "province": "Munster",
    "latitude": 52.35,
    "longitude": -9.6833
  },
]
```

This script requires the Python library BeautifulSoup.
