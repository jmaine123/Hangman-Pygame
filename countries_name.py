from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree, html
import time
import requests
import re
import pandas as pd
import requests
import json
import time
from selenium.webdriver.common.by import By
from dataclasses import dataclass, asdict
from tqdm import tqdm
import pickle


countries_dict = {"Countries": []}

def contains_number(string):
    for i in list(string):
        if i.isdigit():
            return True
    return False

    

class Scraper:
    
    def getInfo(self):
        url = f'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        s = soup.prettify()
        dom = etree.HTML(str(soup))
        countries = dom.xpath('//tbody/tr/td[2]/text()')
        
        # countries_dict["Courses"] = countries

        for country in countries:
            print(country)            
            if contains_number(country) == False:
                countries_dict["Countries"].append(country)
    
    



def main():
    project = Scraper()
    project.getInfo()
    
    # print(countries_dict)

    # opening file in write mode (binary) 
    file = open("countries.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(countries_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()