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


flowers_dict = {"Flowers": []}

# def contains_number(string):
#     for i in list(string):
#         if i.isdigit():
#             return True
#     return False

    

class Scraper:
    
    def getInfo(self):       
        url = f'https://www.flowers-cs.com/type_of_flowers.html#menu-item-385'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        s = soup.prettify()
        print(s)
        dom = etree.HTML(str(soup))
        flowers = dom.xpath('//ul[@id="menu-types-of-flowers"]/li/a/span/text()')
        

        for flower in flowers:
            # print(flower)           
            flowers_dict["Flowers"].append(flower)
    
    



def main():
    project = Scraper()
    project.getInfo()
    
    print(flowers_dict)

    # opening file in write mode (binary) 
    file = open("flowers.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(flowers_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()