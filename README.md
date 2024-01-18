A python script to webscrape the wikipedia page containing a list of [Irish towns](https://en.wikipedia.org/wiki/List_of_towns_and_villages_in_the_Republic_of_Ireland), their coordinates and the provinces they belong to.

This script requires Python's BeautifulSoup library and it generates a JSON file with the following structure:

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

The script was created to populate the fictitious website [YelpCamp](https://github.com/alexandrearantes1/yelp-camp) and test it's functionality and general looks.
