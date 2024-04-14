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


dc_dict = {"DC Comics": []}

def contains_number(string):
    for i in list(string):
        if i.isdigit():
            return True
    return False

    

class Scraper:
    def getInfo(self):
        
        for i in range(1,14):
            url = f'https://www.dc.com/characters?page={i}'
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            s = soup.prettify()
            dom = etree.HTML(str(soup))
            characters = dom.xpath('//div[contains(@class, "item-primary")]/a/@aria-label')

            for character in characters:
                
                if contains_number(character) == False:
                    dc_dict["DC Comics"].append(character)
    
    



def main():
    project = Scraper()
    project.getInfo()
    
    print(dc_dict)

    # opening file in write mode (binary) 
    file = open("dc_characters.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(dc_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()