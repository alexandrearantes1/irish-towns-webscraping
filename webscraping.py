#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 21:57:20 2021

@author: alexandrearantes
"""

from bs4 import BeautifulSoup as bs
import requests
import json
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_content_value (row_data):
    if row_data.find("li"):
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all("li")]
    elif row_data.find("br"):
        return [text for text in row_data.stripped_strings]
    else: 
        return row_data.get_text(" ", strip=True).replace("\xa0", " ")

def get_info_box(url):
    try :
        r = requests.get(url)
        soup = bs(r.content, features="lxml")
        
        # clean_tags(soup)
        
        town = soup.find(class_="org").text
        
        province = soup.select(".infobox-data")[1].contents[0].text
        geo = soup.select(".geo")[0].text.split(";")
        
        latitude = float(geo[0])
        longitude = float(geo[1].lstrip())
            
        print(town)
        print(province)
        print(latitude)
        print(longitude)
        
        town_info = {}
        
        town_info["town"] = town
        town_info["province"] = province
        town_info["latitude"] = latitude
        town_info["longitude"] = longitude
                    
        return town_info
    except Exception as e:
        print(e)


def clean_tags(soup):
    for tag in soup.find_all(["sup", "span"]):
        tag.decompose()


def save_data (title, data):
    with open(title, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
def load_data(title):
    with open(title, encoding="utf-8") as f:
        return json.load(f)    


# Request the wiki page with Irish Cities
r = requests.get("https://en.wikipedia.org/wiki/List_of_towns_and_villages_in_the_Republic_of_Ireland")

# convert the contents of the page to BeatifulSoup object

soup = bs(r.content, features="lxml")

# select the links inside the italic elements with classes .wikitable .sortable of the page
# all <i> <a> elements with classes .wikitable and .sortable are movies names with their links

base_path = "https://en.wikipedia.org/"

towns = soup.select(".mw-parser-output .hlist-separated ul li a")

towns_list = []

total_towns = len(towns)

for index, town in enumerate(towns):
 
    try:
        relative_path = town['href']
        full_path = base_path + relative_path
        town_name = town['title']
        
        towns_list.append(get_info_box(full_path))
        print(town)
        
    except Exception as e:
        print("---------------")
        print("Error: " + str(e))
        print("Town: " + title)
        print("---------------")
    print(f'total: {index} / {total_towns}');
    print("{:.2f}%".format(index / total_towns * 100))
    

save_data("irish_towns.json", towns_list)
    