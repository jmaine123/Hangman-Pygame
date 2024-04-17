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


disney_dict = {"Disney": []}

def contains_number(string):
    for i in list(string):
        if i.isdigit():
            return True
    return False

    

class Scraper:
    def getInfo(self):
        
        for i in range(1,2):
            url = f'https://www.imdb.com/list/ls026785255/?st_dt=&mode=detail&page={i}'
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            s = soup.prettify()
            dom = etree.HTML(str(soup))
            movies = dom.xpath('//h3[@class="lister-item-header"]/a/text()')

            for movie in movies:
                
                if contains_number(movie) == False:
                    disney_dict["Disney"].append(movie)
    
    



def main():
    project = Scraper()
    project.getInfo()
    
    print(disney_dict)

    # opening file in write mode (binary) 
    file = open("disney.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(disney_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()